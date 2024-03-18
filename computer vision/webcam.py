import cv2
cam = cv2.VideoCapture(0) #index value of webcam
while cam.isOpened():
    state, frame = cam.read() # state tells about image from webcame
    if not state:
        print("no frame")
        break
    cv2.imshow("cam1", frame)
    if cv2.waitKey(1) == 27: #27 is for exit button. or == ord("q")
        break

cam.release()
cv2.destroyAllWindows()
    