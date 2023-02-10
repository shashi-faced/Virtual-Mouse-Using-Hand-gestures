import cv2
import numpy as np


def click_event(event, x, y, flags, param):
    print(event, x, y)
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 3,(0,0,355), -1)
        cv2.imshow("outout",img)
        cv2.waitKey(0)

# img  = np.zeros((500,612,3), np.uint8)

img = cv2.imread('/home/sk/Desktop/first.jpg',1)
cv2.namedWindow('image')
cv2.setMouseCallback('image', click_event)
while True:
    cv2.imshow("outout",img)
    if cv2.waitKey(0)  & 0xFF == ord('q'):
        break

cv2.destroyAllWindows() 