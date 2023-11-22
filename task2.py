import cv2 as cv
# Task 2 
# Object Detection
cascade_path='cars.xml'
car_cascade=cv.CascadeClassifier(cascade_path)

capture=cv.VideoCapture('Video/carsVideo.mp4')

while True:
    ret,frame=capture.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    # Detect car vehicle from frame
    cars=car_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3,minSize=(25,25))
    
    for (x,y,w,h) in cars:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        
    cv.imshow('vehicle',frame)
    
    if cv.waitKey(27) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()