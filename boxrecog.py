#Detect faces and draw square around it
import cv2

face_cascade = cv2.CascadeClassifier("cascade.xml")

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    face = face_cascade.detectMultiScale(gray,1.02,6)
    for x,y,w,h in face:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(224, 213, 56),2)

    cv2.imshow("Face detected",frame)
    if(cv2.waitKey(1)==ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
