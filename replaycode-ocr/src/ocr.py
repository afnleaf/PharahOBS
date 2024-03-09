import cv2 as cv
import numpy as np
import pandas as pd
import pytesseract
from MTM import matchTemplates, drawBoxesOnRGB
from PIL import Image


# process input image genius comment
# just turn it gray ez
def pre_process_input_image(image):
    # grayscale it
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # thresholding? not needed?
    #image = cv.threshold(image, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]
    return image


# how to solve the copy problem
# process each of the matched replaycode images for clearer text
def process_cropped_image(image):
    # invert
    image = cv.bitwise_not(image)
    # resize 2x
    image = cv.resize(image, (0,0), fx=24, fy=24)
    # remove noise
    image = cv.medianBlur(image, 5)
    #blur = cv.GaussianBlur(gray, (0,0), sigmaX=33, sigmaY=33)
    #divide = cv.divide(gray, blur, scale=255)
    # thresholding
    image = cv.threshold(image, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]
    # dilation
    kernel = np.ones((5,5),np.uint8)
    image = cv.dilate(image, kernel, iterations = 1)
    # erosion
    image = cv.erode(image, kernel, iterations = 1)
    # opening - erosion followed by dilation
    image = cv.morphologyEx(image, cv.MORPH_OPEN, kernel)
    # canny
    #image = cv.Canny(image, 100, 200)
    return image


# process the string given by the tesseract model
def process_text(text):
    n = len(text)
    start = 0
    end = 0

    # find last non alpha numeric character in first chunk before space
    for i in range(0, n):
        if not text[i].isalnum():
            start = i + 1
        if text[i] == " ":
            break
        
    # find last space after chunk
    for i in range(start, n):
        if text[i] == " ":
            end = i
            break
        # in case end is reached before space
        end = i
    
    # return sliced text
    return text[start:end].upper()


# print replay code list, not used
def print_codes(replaycodes):
    for code in replaycodes:
        print(code)


# process what is given by attachement.read()
async def load_image_from_discord(image_data):
    array = np.asarray(bytearray(image_data), dtype=np.uint8)
    image = cv.imdecode(array, -1)
    return image


def load_template(template_filename):
    template = cv.imread(template_filename, cv.IMREAD_GRAYSCALE)
    assert template is not None, "file could not be read, check with os.path.exists()"
    return template


# create some templates
def create_templates(template):
    # where we store our templates
    list_of_templates = []           

    j = 0
    for i in range(1, 20, 3):
        template_resized = cv.resize(template, (0,0), fx=1/i, fy=1/i)
        list_of_templates.append((f"{j}", template_resized))
        j += 1
            
    return list_of_templates


# match templates to input image
def template_match(img_input, templates):
    # the directory we will store our images
    # should go in a config file along with other logging related stuff
    output_append = "/app/output/"


    # process input image
    img_final = pre_process_input_image(img_input)
    cv.imwrite(output_append + "input_final.png", img_final)
    # get width and height of image to check later
    w, h = img_final.shape[::-1]
    #print(f"w:{w} h:{h}")

    # check for template size larger than input image
    list_of_templates = []
    j = 0
    for template in templates:
        wr, hr = template[1].shape[::-1]
        #print(f"wr:{wr} hr:{hr}")
        if wr <= w and hr <= h:
            list_of_templates.append(template)
            # write for log
            output_filename = output_append + "template" + str(j) + ".png"
            cv.imwrite(output_filename, template[1])

    # find matches and store locations in a pandas dataframe
    hits = matchTemplates(list_of_templates,  
               img_final,  
               method=cv.TM_CCOEFF_NORMED,  
               N_object=float("inf"),   
               score_threshold=0.79,   
               maxOverlap=0.25,   
               searchBox=None)

    # draw boxes around templates
    image_boxes = drawBoxesOnRGB(img_input, 
               hits, 
               boxThickness=2, 
               boxColor=(255, 255, 00), 
               showLabel=True,  
               labelColor=(255, 255, 0), 
               labelScale=0.5 )
    output_filename = "/app/output/boxes.png"
    cv.imwrite(output_filename, image_boxes)

    # where we are storing all the crop data
    list_of_crops = []

    # find out which template matched
    # get locations of matches out of the dataframe
    print(hits)
    dataframe = pd.DataFrame(hits)
    #template_indices = dataframe['TemplateName'].tolist()
    bboxes = dataframe['BBox'].tolist()

    for index, box in enumerate(bboxes):        
        print(box)
        # starting location of crop
        ptx = box[0]
        pty = box[1]
        pt = (ptx, pty)
        # how much to add to start location in width and height
        # scale width more than height
        width = int(box[2] * 7)
        height = int(box[3] * 1.1)
        crop = img_final[pt[1]:pt[1] + height, pt[0]:pt[0] + width]
        # before
        output_filename_before = output_append + "before" + str(index) + ".png"
        cv.imwrite(output_filename_before, crop)
        # process our replay code crops
        crop_final = process_cropped_image(crop)
        list_of_crops.append(crop_final)
        # after
        output_filename_after = output_append + "after_" + str(index) + ".png"
        cv.imwrite(output_filename_after, crop_final)

    return list_of_crops


# gonna need to keep working on this to make it better
def process_codes(list_of_crops):
    # list of replay code text
    replaycodes = []

    for crop in list_of_crops:
        # output code as text
        text = pytesseract.image_to_string(crop, lang='eng', config='--psm 6')
        print(text)
        code = process_text(text)
        # avoid duplicates
        if code not in replaycodes:
            replaycodes.append(code)

    return replaycodes


# main function, testing mostly
def main():
    input_filename="images/Screenshot_3.png"
    #input_filename="images/image_proc4.jpg"
    template_filename="images/template_large.png"
    image = cv.imread(input_filename)
    template = load_template(template_filename)
    crops = template_match(image, template)
    replaycodes = process_codes(crops)
    print_codes(replaycodes)
    #parse_image(input_filename, template_filename)

    
# Default notation
if __name__ == "__main__":
    main()
