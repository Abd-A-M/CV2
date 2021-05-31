import cv2
# capture frames
cap = cv2.VideoCapture(0)
#set video type
res = cv2.VideoWriter_fourcc(*"XVID")
write = cv2.VideoWriter("newVideo.avi", res,60.0,(640,480))
# change the width and hight of frames
cap.set(3, 400)
cap.set(4, 400)
while True:
    ret ,frame = cap.read()
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FPS))
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        #write frames using object 
        write.write(frame)
        gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
        cv2.imshow("frame",gray)
        if cv2.waitKey(1) == ord("z"):
            cv2.destroyAllWindows()
            break
cap.release()
write.release()
cv2.destroyAllWindows()
