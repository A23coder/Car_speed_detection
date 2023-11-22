# capture video and run 
import cv2 as cv

# Task 1
# Input Video
def captureVideo():
    capture=cv.VideoCapture('Video/carsVideo.mp4')
    while True:
        ret,frame=capture.read()
        if ret==False:
            break
        cv.imshow('video',frame)
        if cv.waitKey(20) & 0xFF == ord('q'):
            break
    capture.release()
    cv.destroyAllWindows()
    
if __name__=="__main__":
    captureVideo()