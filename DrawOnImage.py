import cv2
import numpy as np

im = np.zeros([500,500,3])
im = cv2.line(im,(0,0),(256,256),(255,255,255))
im = cv2.arrowedLine(im,(256,256),(256,0),(255,255,255),2)
#use the thickness = to -1 to make a FILLED RECTANGLE
im = cv2.rectangle(im,(10,10),(256,256),(255,255,255),2)
im = cv2.circle(im,(256,256),256,(255,255,255),-1)
font = cv2.FONT_ITALIC
im = cv2.putText(im,"abdullah" , (20,200),font,2,(255,0,0),2)
cv2.imshow("image",im)
cv2.waitKey(0)
cv2.destroyAllWindows()
