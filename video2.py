import cv2,time


# to build a program for facedetect as per frames from the video capture

video=cv2.VideoCapture(0)

check,frame=video.read()

# check contains the boolean value returnd from .read()

print(check)
print(frame)

time.sleep(3)
cv2.imshow("capture",frame)
cv2.waitKey(0)
video.release()
cv2.destroyAllWindows()

