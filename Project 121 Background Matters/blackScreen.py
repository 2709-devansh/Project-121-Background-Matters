import cv2
import numpy as np
import keyboard

capture = cv2.VideoCapture(0)
img = cv2.imread("bg.jpg")

while (capture.isOpened()):
    ret, bg = capture.read()
    if not ret:
        break
    bg = np.flip(bg, axis = 1)

    bg = cv2.resize(bg, (640, 480))
    img = cv2.resize(img, (640, 480))

    lowerBlack = np.array([0, 0, 0])
    upperBlack = np.array([104, 153, 70])

    mask = cv2.inRange(bg, lowerBlack, upperBlack)
    result = cv2.bitwise_and(bg, bg, mask = mask)
    
    f = bg - result
    f = np.where(f == 0, img, f)

    cv2.imshow('Output', f)

    cv2.waitKey(1)

    if keyboard.is_pressed('q'):
        break

capture.release()
cv2.destroyAllWindows()