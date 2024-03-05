import pytesseract
from pytesseract import Output
from PIL import Image
import cv2 as cv
import numpy as np
import re


def pre_process_input_image(image):
    # grayscale it
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # thresholding
    #image = cv.threshold(image, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]
    return image


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
    #opening - erosion followed by dilation
    image = cv.morphologyEx(image, cv.MORPH_OPEN, kernel)
    # canny
    #image = cv.Canny(image, 100, 200)

    return image


def process_text1(text):
    pattern = r'[^a-zA-Z0-9]+\s*(.*)'

    # Search for the pattern in the input string
    match = re.search(pattern, text)

    if match:
        # Extract the desired chunk
        extracted_chunk = match.group(1)
        print("Extracted chunk:", extracted_chunk)
    else:
        print("Pattern not found in the input string.")


# process the string given by the tesseract engine
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


# print replay codes
def print_codes(replaycodes):
    for code in replaycodes:
        print(code)


def parse_image(input_filename, template_filename):
    output_append = '/app/output/result'
    
    # load image
    img_rgb = cv.imread(input_filename)
    assert img_rgb is not None, "file could not be read, check with os.path.exists()"

    #img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    #img_bifilter = cv.bilateralFilter(img_gray,9,75,75)
    img_final = pre_process_input_image(img_rgb)
    cv.imwrite(output_append + "final.png", img_final)

    # load template
    template = cv.imread(template_filename, cv.IMREAD_GRAYSCALE)
    #template = cv.resize(template, (0,0), fx=1.5, fy=1.5) 
    assert template is not None, "file could not be read, check with os.path.exists()"
    # template_final = pre_process_image(template)
    w, h = template.shape[::-1]

    # match template to input
    res = cv.matchTemplate(img_final, template, cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)

    # list of replay codes
    replaycodes = []

    # rectangle around it
    outbound_w = 115
    outbound_h = 25
    i = 0
    for pt in zip(*loc[::-1]):
        #cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
        #cv.rectangle(img_rgb, pt, (pt[0] + outbound_wplus, pt[1] + outbound_hplus), (0,255,0), 2)
        newptx = pt[0] - 2
        newpty = pt[1] - 2
        newpt = newptx, newpty
        #cv.rectangle(img_rgb, newpt, (newpt[0] + outbound_w, newpt[1] + outbound_h), (0,255,0), 2)

        # Crop the image around the contour
        crop = img_final[newpt[1]:newpt[1] + outbound_h, newpt[0]:newpt[0] + outbound_w]
        
        # process cropped image
        output_filename_before = output_append + "_before_" + str(i) + ".png"
        # before
        cv.imwrite(output_filename_before, crop)
        crop_final = process_cropped_image(crop)
        # after
        output_filename_after = output_append + "_after_" + str(i) + ".png"
        cv.imwrite(output_filename_after, crop_final)


        # output code as text
        text = pytesseract.image_to_string(crop_final)
        code = process_text(text)
        # avoid duplicates
        if code not in replaycodes:
            replaycodes.append(code)

        i+=1

    # print all replay codes
    print_codes(replaycodes)
    
    # print codes to file Todo

# main function
def main():
    input_filename = 'image_proc4.jpg'
    template_filename = 'template_proc.jpg'
    parse_image(input_filename, template_filename)

# Default notation
if __name__ == "__main__":
    main()

