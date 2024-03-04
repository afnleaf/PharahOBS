
'''
image = cv2.imread(input_filename)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply edge detection (you might need to fine-tune parameters)
edges = cv2.Canny(gray, threshold1=30, threshold2=100)

# Find contours in the edged image
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Loop over the contours
i = 0
for contour in contours:
    # Get the coordinates and dimensions of the contour
    x, y, w, h = cv2.boundingRect(contour)
    
    # Crop the image around the contour
    symbol = image[y:y+h, x:x+w]
    
    output_filename = output_append + str(i) + ".png"
    cv2.imwrite(output_filename, symbol)
    i+=1
    # Save or display the cropped symbol
    #cv2.imshow('Symbol', symbol)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
'''


'''
# Load the image
image = cv2.imread(input_filename)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite(output_append + "test1.png", gray)

# Apply edge detection (you might need to fine-tune parameters)
edges = cv2.Canny(gray, threshold1=30, threshold2=100)
cv2.imwrite(output_append + "test2.png", edges)

# Find contours in the edged image
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Load the symbol template
template = cv2.imread(template_filename, 0)  # Make sure to replace 'your_template_symbol.jpg' with the filename of your template symbol

# Loop over the contours
for contour in contours:
    # Get the coordinates and dimensions of the contour
    x, y, w, h = cv2.boundingRect(contour)
    
    # Crop the image around the contour
    symbol_roi = gray[y:y+h, x:x+w]
    
    # Resize the symbol ROI to match the size of the template
    resized_symbol_roi = cv2.resize(symbol_roi, (template.shape[1], template.shape[0]))
    
    # Perform template matching
    result = cv2.matchTemplate(resized_symbol_roi, template, cv2.TM_CCOEFF_NORMED)
    
    # Define a threshold for template matching results
    threshold = 0.8
    
    # Find locations where the template matches the symbol ROI
    locations = cv2.findNonZero((result >= threshold).astype('uint8'))
    
    if locations is not None:
        # If the symbol is found, draw a rectangle around it
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    output_filename = output_append + "1231" + ".png"
    cv2.imwrite(output_filename, image)

'''

'''
filename = 'image_proc.jpg'
img = cv2.imread(filename)
d = pytesseract.image_to_data(img, output_type=Output.DICT)
n_boxes = len(d['level'])
for i in range(n_boxes):
    if (d['text'][i] != ""):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2) # in-place operation
        print("Text:", d['text'][i], "Confidence:", d['conf'][i])

output_filename = '/app/output/result.jpg'
cv2.imwrite(output_filename, img)
'''

'''
filename = 'image_proc.jpg'

# read the image and get the dimensions
img = cv2.imread(filename)
h, w, _ = img.shape # assumes color image

# run tesseract, returning the bounding boxes
boxes = pytesseract.image_to_boxes(img) # also include any config options you use
print(boxes)

# draw the bounding boxes on the image
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)


output_filename = '/app/output/image_with_boxes.jpg'
cv2.imwrite(output_filename, img)

'''


'''
img_path1 = 'Screenshot_1.png'
text = pytesseract.image_to_string(img_path1,lang='eng')
print(text)

img_path2 = 'image_proc.jpg'
#boxes = pytesseract.image_to_boxes(img_path2)
#print(boxes)

# Get a searchable PDF
pdf_path = '/app/output/test.pdf'
pdf = pytesseract.image_to_pdf_or_hocr(img_path2, extension='pdf')
with open(pdf_path, 'w+b') as f:
    f.write(pdf) # pdf type is bytes by default
'''