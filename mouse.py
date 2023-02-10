import cv2
import numpy as np


def click_event(event, x, y, flags, param):
    print(event, x, y)
    if event == cv2.EVENT_LBUTTONDOWN:
        strxy = str(x) + ',' + str(y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,strxy, (x,y), font, 1 ,(700,700,3), 2)
        cv2.imshow("outout",img)
        cv2.waitKey(0)

img  = np.zeros((700,700,3), np.uint8)

cv2.namedWindow('image')
cv2.setMouseCallback('image', click_event)
while True:
    cv2.imshow("outout",img)
    if cv2.waitKey(0)  & 0xFF == ord('q'):
        break

cv2.destroyAllWindows() 