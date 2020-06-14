import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("news.jpg")

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)

for x,y,w,h in face:
    imag=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,4,0),5)

resized_img=cv2.resize(imag,(int(imag.shape[1]/3),int(imag.shape[0]/3)))

cv2.imshow("face",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()