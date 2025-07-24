import cv2

video = cv2.VideoCapture('http://192.168.0.103:8080/video')

while True:
    ret, frame = video.read()
    resize_fr = cv2.resize(frame, (640, 480))

    cv2.imshow('Camera', resize_fr)

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()