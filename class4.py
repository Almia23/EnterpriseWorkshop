import cv2
import matplotlib.pyplot as plt
cap=cv2.VideoCapture(0) #internal is 0, external is 1

ret,frame = cap.read()
plt.imshow(frame)
plt.title("Image cap from camera")
plt.show()

cap.release()