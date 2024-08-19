import cv2
img = cv2.imread("cat.jpeg")
grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Cat image",grayimg)

cv2.waitKey(0) #any key accepted to close
cv2.destroyAllWindows()