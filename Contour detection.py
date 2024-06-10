import os 
import cv2

#importing and reszizing image
image_path= os.path.join('Tutorial_edits\People swimming.jpg') #paste the path of the image inside the invited commas. 
image=cv2.imread(image_path)
r_image=cv2.resize(image, (800,400))

#contour detection

#step 1: Converting to Grayscale
image_gray=cv2.cvtColor(r_image, cv2.COLOR_RGB2GRAY)

# Step 2: Increasing threshold
ret, thresh= cv2.threshold(image_gray, 80, 255, cv2.THRESH_BINARY_INV) #increases the contrast of the black and white image

#Step3 : Contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #detects the contours available in the image.

for cnt in contours:
    if cv2.contourArea(cnt) > 50:
       # cv2.drawContours(r_image, cnt, -1, (0,255,0), 1) ///This ine of code makes the contour of th eimage green
        x1, y1, w, h= cv2.boundingRect(cnt) ##This line of code draws a rectangle around the detected articles in the image
        cv2.rectangle(r_image,(x1,y1),(x1+w, y1+h), (0,255,0),2)



cv2.imshow('frame', r_image)
cv2.imshow('frame_gray', image_gray)
cv2.imshow('frame_thresh', thresh)
cv2.waitKey(0)


