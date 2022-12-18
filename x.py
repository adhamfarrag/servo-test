import numpy as np
import cv2

cap = cv2.VideoCapture('http://192.168.0.140:9000/')

while (cap.isOpened()):
    ret, image = cap.read()
    loadedImage = cv2.imdecode(image, cv2.IMREAD_COLOR)
    cv2.imshow('frame', loadedImage)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
