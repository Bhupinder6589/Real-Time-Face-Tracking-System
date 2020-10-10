import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

capture=cv2.VideoCapture(0,cv2.CAP_DSHOW)
while 1:
    ret,img=capture.read()
    print(ret,img)

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(img,1.3,5)

    for x,y,w,h in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),1)

    cv2.imshow('capture',img)
    keycode=cv2.waitKey(1)
    print(keycode)
    if keycode==ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
