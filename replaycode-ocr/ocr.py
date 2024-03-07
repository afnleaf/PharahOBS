import pytesseract
from pytesseract import Output
from PIL import Image
import cv2 as cv
import urllib.request
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
    # opening - erosion followed by dilation
    image = cv.morphologyEx(image, cv.MORPH_OPEN, kernel)
    # canny
    #image = cv.Canny(image, 100, 200)

    return image


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


async def load_image_from_discord(image_data):
    array = np.asarray(bytearray(image_data), dtype=np.uint8)
    image = cv.imdecode(array, -1)
    return image

def load_template(template_filename):
    template = cv.imread(template_filename, cv.IMREAD_GRAYSCALE)
    assert template is not None, "file could not be read, check with os.path.exists()"
    return template


def parse_image(img_input, template):
    #print("parse_image")
    output_append = '/app/output/result'    
    #img_rgb = cv.imread(input_filename)
    #assert img_rgb is not None, "file could not be read, check with os.path.exists()"
    #img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    #img_bifilter = cv.bilateralFilter(img_gray,9,75,75)

    # load image
    img_final = pre_process_input_image(img_input)
    cv.imwrite(output_append + "final.png", img_final)

    # load template
    w, h = template.shape[::-1]

    # match template to input
    # need multiple template sizes for different input image pixel densities
    res = cv.matchTemplate(img_final, template, cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)

    # list of replay codes
    replaycodes = []

    # rectangle around location of matched template
    outbound_w = 115
    outbound_h = 25
    i = 0
    # loop through each locations
    for pt in zip(*loc[::-1]):
        newptx = pt[0] - 2
        newpty = pt[1] - 2
        newpt = newptx, newpty

        # Crop the image around the contour
        crop = img_final[newpt[1]:newpt[1] + outbound_h, newpt[0]:newpt[0] + outbound_w]
        
        # process cropped image
        #output_filename_before = output_append + "_before_" + str(i) + ".png"
        # before
        #cv.imwrite(output_filename_before, crop)
        crop_final = process_cropped_image(crop)
        # after
        #output_filename_after = output_append + "_after_" + str(i) + ".png"
        #cv.imwrite(output_filename_after, crop_final)

        # output code as text
        text = pytesseract.image_to_string(crop_final)
        code = process_text(text)
        # avoid duplicates
        if code not in replaycodes:
            replaycodes.append(code)

        i+=1

    # print all replay codes
    #print_codes(replaycodes)
    
    return replaycodes


# main function
def main():
    input_filename = 'images/image_proc4.jpg'
    template_filename = 'images/template_proc.jpg'
    parse_image(input_filename, template_filename)


# Default notation
if __name__ == "__main__":
    main()