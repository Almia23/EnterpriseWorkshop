#Detect faces and draw square around it
import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("group.jpg")
grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face = face_cascade.detectMultiScale(grayimg,1.03,6)

for x,y,w,h in face:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(224, 213, 56),2)
    
cv2.imshow("Face detected in img",img)

cv2.imshow("Group img grayscale",grayimg)
cv2.waitKey(0)
cv2.destroyAllWindows()