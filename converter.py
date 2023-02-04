import cv2
import numpy as np

video = cv2.VideoCapture('')
print("video open")

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

output = cv2.VideoWriter('', fourcc, 20.0, (1280, 720))
print("writer configured")
count = 0
while video.isOpened():
    count = count + 1
    print(f"processing frame{count}")
    ret, frame = video.read()
    if ret:
        frame = cv2.resize(frame, (1280, 720), interpolation=cv2.INTER_CUBIC)
        output.write(frame)
    else:
        break

video.release()
output.release()
cv2.destroyAllWindows()


