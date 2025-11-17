# OpenCV program to detect face in real time
# import libraries of python OpenCV
# where its functionality resides
import cv2

import time

# Trained XML classifiers describes some features of some
# object we want to detect a cascade function is trained
# from a lot of positive(faces) and negative(non-faces)
# images.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# capture frames from a camera
cap = cv2.VideoCapture(0)

stamp = time.time()

# loop runs if capturing has been initialized.
while 1:
    stamp = time.time()

    # reads frames from a camera
    ret, img = cap.read()

    # convert to gray scale of each frames
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detects faces of different sizes in the input image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        # To draw a rectangle in a face
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        cv2.circle(img,(int(x+w/2),int(y+h/2)),5,(255,255,0),2)

    cv2.imwrite('image.jpg', img)

    print(time.time() - stamp)
