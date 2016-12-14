import numpy as np
import cv2

img = cv2.imread("Test1.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
surf = cv2.SURF()
surf.hessianThreshold = 10000

kp, des = surf.detectAndCompute(img, None)
img2 = cv2.drawKeypoints(img, kp, None, (255, 0, 0), 4)

cv2.imshow("SURF", img2)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()