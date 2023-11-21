import cv2 as cv
capture = cv.VideoCapture('Video/new.mp4')
while True:
    ret, frame=capture.read()
    height,width=frame.shape[:2]
    cv.imshow('video',frame)
    if cv.waitKey(20) &  0xFF == ord('q'):
        break
print(height,width)
capture.release()
cv.destroyAllWindows()