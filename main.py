import cv2


# Face recognition 
face_haar_cascade = cv2.CascadeClassifier('/home/juto/Desktop/pythonProject/haarcascade_frontalface_default.xml')

image = cv2 .imread('images/somi.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


faces = face_haar_cascade.detectMultiScale(gray, 1.1, 4)

for(x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h),
                  (0.255,0), 5)
    cv2.imshow("Faces", image)

cv2.waitKey()