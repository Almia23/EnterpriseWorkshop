import cv2

img=cv2.imread("cat.jpeg")
print(img.shape)
while True:
    cv2.imshow("cat image",img)
    if(cv2.waitKey(1)==ord('q')):
        break
cv2.destroyAllWindows()
    
#testing
