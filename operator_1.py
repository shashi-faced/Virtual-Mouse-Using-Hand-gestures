import cv2
import numpy as np

img1 = cv2.imread('/home/sk/Desktop/first.jpg',1)
img2 = cv2.imread('/home/sk/Desktop/second.jpg',1)

# bitimg = cv2.bitwise_and(img1,img2)
while True: 
    
    cv2.imshow("output", img1)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.imshow("output", img2)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
            # cv2.imshow("ou",bitimg)
            # if cv2.waitKey(0) & 0xFF == ord('q'):
            #     break
cv2.destroyAllWindows()