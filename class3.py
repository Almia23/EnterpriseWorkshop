import cv2
img = cv2.imread("cat.jpeg")
grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,binimg=cv2.threshold(grayimg,150,255,cv2.THRESH_BINARY)

print(img.shape)
print(img.ndim)


while True:
    cv2.imshow("cat image",binimg)
    if(cv2.waitKey(1)==ord('q')):
        break
cv2.destroyAllWindows()
    