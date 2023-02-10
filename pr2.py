import cv2
from cv2 import VideoCapture
from cv2 import waitKey

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
out = cv2.VideoWriter('onet_10.mp4v', fourcc, 20.0 , (600,480)) 


print(cap.isOpened())
while cap:
    ret,frame =  cap.read()

    if(ret == True):

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow("output",frame)

        out.write(frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("ret value is false")
        break
cap.release()
out.release()
cv2.destroyAllWindows()