import pytesseract
from pytesseract import Output
from PIL import Image
import cv2 as cv
import numpy as np
#from matplotlib import pyplot as plt

# Load the image
input_filename = 'image_proc.jpg'
#input_filename = 'result0.png'
output_append = '/app/output/result'
template_filename = 'template_proc.jpg'

# load image
img_rgb = cv.imread(input_filename)
assert img_rgb is not None, "file could not be read, check with os.path.exists()"
# grayscale it
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
# load template
template = cv.imread(template_filename, cv.IMREAD_GRAYSCALE)
assert template is not None, "file could not be read, check with os.path.exists()"
w, h = template.shape[::-1]



# match template to input
res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)

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
    crop = img_rgb[newpt[1]:newpt[1] + outbound_h, newpt[0]:newpt[0] + outbound_w]
    output_filename = output_append + str(i) + ".png"
    cv.imwrite(output_filename, crop)

    crop_gray = cv.cvtColor(crop, cv.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(crop_gray)
    print(text)

    i+=1


cv.imwrite('/app/output/res.png',img_rgb)



