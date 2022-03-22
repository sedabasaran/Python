#OpenCv-Capture Video from Camera

import cv2
cap = cv2.VideoCapture(0)
cap.set(3,640) #set width 
cap.set(4,480) #set hight
while True: 
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
    cv2.imshow("capture",frame)
    cv2.imshow("gray",gray)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

   

cap.release()
cv2.destroyAllWindows()
