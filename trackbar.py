import cv2
import numpy as np

def nothing(x):
    print(x)

img = np.zeros((100, 100, 3), np.uint8)
cv2.namedWindow('image')

#adding tranbar
cv2.createTrackbar('Blue', 'image', 0, 255, nothing)
cv2.createTrackbar('Green', 'image', 0, 255, nothing)
cv2.createTrackbar('Red', 'image', 0, 255, nothing)

while True:
    cv2.imshow('image', img)
    k  = cv2.waitKey(1)
    if k == ord('q'):
        break
    
    b = cv2.getTrackbarPos('Blue', 'image')
    g = cv2.getTrackbarPos('Green', 'image')    
    r = cv2.getTrackbarPos('Red', 'image')
    
    img[:] = [b, g, r]

cv2.destroyAllWindows()