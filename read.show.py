# This function to read and show images
#
import cv2

im = cv2.imread("10.jpg")
while True:
    cv2.imshow("image", im)
    # pass 0 to wait input from user, pass e.g.5000
    # wait for 5 sec.
     input = cv2.waitKey(0)
     # if user press esc 
    if input == 27:
        # cv2.destroyAllWindows()
        im = cv2.imread("11.jpg")
        cv2.imshow("image", im)
        break
       # if user press "z" button 
    if input == ord("z"):
        cv2.destroyAllWindows()
        break
    # else:
    #     cv2.destroyAllWindows()
    #     print("hello")
    #     break
