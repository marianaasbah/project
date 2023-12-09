import cv2 as cv
from pynput.keyboard import Key, Controller
from detectors_world import DetectorCreator
from time import sleep

cap = cv.VideoCapture(0)

creator = DetectorCreator()

hand = creator.getDetector("hand")

keyboard = Controller()

def check_index_finger(landmarks):
    if len(landmarks) != 0:
        if (landmarks[8][2] < 100):
            keyboard.release(Key.right)
            keyboard.release(Key.left)
            print("UP")
            keyboard.press(Key.up)
            sleep(0.05)
        elif (350>landmarks[8][2] > 100) and (landmarks[8][1] <200):
            keyboard.release(Key.up)
            keyboard.release(Key.right)
            print("LEFT")
            keyboard.press(Key.left)
            sleep(0.05)
        elif (350>landmarks[8][2] > 100) and (landmarks[8][1] >440):
            keyboard.release(Key.up)
            keyboard.release(Key.left)
            print("RIGHT")
            keyboard.press(Key.right)
            sleep(0.05)
        elif (landmarks[8][2] > 350) and (landmarks[8][1] <200):
            keyboard.release(Key.right)
            print("LEFT_UP")
            keyboard.press(Key.up)
            keyboard.press(Key.left)
            sleep(0.05)
        elif (landmarks[8][2] > 350) and (landmarks[8][1] >440):
            keyboard.release(Key.left)
            print("RIGHT_UP")
            keyboard.press(Key.up)
            keyboard.press(Key.right)
            sleep(0.05)
        elif (150<landmarks[8][2]<350) and (210<landmarks[8][1]<430):
            keyboard.release(Key.left)
            keyboard.release(Key.right)
            keyboard.release(Key.up)
            print("release")
            sleep(0.05)



while True:
    status, img = cap.read()
    img = cv.flip(img,1)
    hand.detect(img, drawOnHand=True)

    lms = hand.locate(img, drawOnHand=True, handsNumber=1)
    check_index_finger(lms)

    cv.line(img, (0, 100), (640, 100), (255, 0, 0), 2)
    cv.line(img, (210, 100), (210, 350), (255, 0, 0), 2)
    cv.line(img, (430, 100), (430, 350), (255, 0, 0), 2)
    cv.rectangle(img, (0, 350), (210, 640), (0, 0, 255), 2)
    cv.rectangle(img, (430, 350), (640, 640), (0, 0, 255), 2)


    
    cv.imshow("Super_Mario Game", img)
    k = cv.waitKey(1)
    
    # if Esc is pressed -> Exit
    if k % 255 == 27:
        break