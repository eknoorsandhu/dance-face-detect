import cv2

# take picture using webcam
camera = cv2.VideoCapture(0)
while True:
    _, frame = camera.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == 27:  # Break loop when 'ESC' is pressed
        cv2.imwrite(filename='capture.jpg', img=frame)
        break
camera.release()
cv2.destroyAllWindows()
