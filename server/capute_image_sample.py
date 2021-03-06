from datetime import datetime

import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, image = cam.read()
    cv2.imshow("Image", image)
    k = cv2.waitKey(1)
    if k != -1:
        break

cv2.imwrite(f"./pigallery2/images/{datetime.now()}.jpg", image)
cam.release()
cv2.destroyAllWindows()
