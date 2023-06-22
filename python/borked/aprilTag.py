import cv2
from cv2 import VideoCapture, imshow, waitKey, destroyWindow
#from apriltag import apriltag

cam = VideoCapture(0)

# detector = apriltag("tagStandard36h11")

while True:
    result, image = cam.read()

    if result:
        imshow("image", image)
    if waitKey(1) & 0xFF == ord('q'):
        break

    #detections = detector.detect(image)

cam.release()
cv2.destroyAllWindows()

# image = cv2.imread(imagepath, cv2.IMREAD_GRAYSCALE)
# detector = apriltag("tagStandard41h12")

# detections = detector.detect(image)
