import numpy as np
import cv2
import time

cap = cv2.VideoCapture("http://202.149.87.56/camera/PasirKalikiIP.m3u8")
fps_time = 0
frame_rate = int(cap.get(5))
print(frame_rate)

while(cap.isOpened()):
    ret, frame = cap.read()

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.putText(frame,"FPS: %f" % (1.0 / (time.time() - fps_time)),(10, 10),  cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0, 255, 0), 2)
    cv2.imshow("Merdeka-Aceh Street",frame)

    fps_time = time.time()
    if cv2.waitKey(frame_rate) == 27:
        break


cap.release()
cv2.destroyAllWindows()
