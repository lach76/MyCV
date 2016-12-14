import cv2

img = cv2.imread("./Test1.jpg")
orb = cv2.ORB()
kp, des = orb.detectAndCompute(img, None)

img2 = cv2.drawKeypoints(img, kp, color=(255, 0, 0), flags=0)
cv2.imshow('ORB', img2)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()