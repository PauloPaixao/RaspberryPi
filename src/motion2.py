# import the necessary packages
import argparse
import datetime
import imutils
import time
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("i1")
ap.add_argument("i2")
args = ap.parse_args()

print args.i1
print args.i2

# resize the frame, convert it to grayscale, and blur it
image1 = cv2.imread(args.i1)
frame = imutils.resize(image1, width=500)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (21, 21), 0)

image2 = cv2.imread(args.i2)
frame2 = imutils.resize(image2, width=500)
gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

# compute the absolute difference between the current frame and first frame
frameDelta = cv2.absdiff(gray2, gray)
thresh = cv2.threshold(frameDelta, 50, 255, cv2.THRESH_BINARY)[1]

# dilate the thresholded image to fill in holes, then find contours on thresholded image
thresh = cv2.dilate(thresh, None, iterations=2)
(cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)


cv2.imwrite('gray_' + args.i2, frameDelta)

# loop over the contours
for c in cnts:
	# if the contour is too small, ignore it
	if cv2.contourArea(c) < 500:
		continue

	# compute the bounding box for the contour, draw it on the frame, and update the text
	(x, y, w, h) = cv2.boundingRect(c)
	cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
	text = "Occupied"

# draw the text and timestamp on the frame
cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
	cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
	(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

	
cv2.imwrite('delta_'+args.i2, frame);
