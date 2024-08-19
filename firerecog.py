
import cv2
from playsound import playsound
import pyttsx3

#text to speech
def myspeakfunc():
    engine = pyttsx3.init()
    engine.say("Fire detected bruh run away")
    engine.runAndWait()

fire_cascade = cv2.CascadeClassifier("fire_detection.xml")

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    fire = fire_cascade.detectMultiScale(gray,1.2,5)
    for x,y,w,h in fire:
        frame = cv2.rectangle(frame,(x-20,y-20),(x+w+20,y+h+20),(224, 213, 56),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        #playsound("firebell.mp3")
        for i in range(2):
            myspeakfunc()
        

    cv2.imshow("Fire detected",frame)
    if(cv2.waitKey(1)==ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
