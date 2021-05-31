import datetime
import cv2

# capture frames
cap = cv2.VideoCapture(0)
# set video type
res = cv2.VideoWriter_fourcc(*"XVID")
write = cv2.VideoWriter("newVideo.avi", res, 60.0, (640, 480))
cap.set(3, 4000)
cap.set(4, 2000)
while True:
    ret, frame = cap.read()
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FPS))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(cap.get(4))
        font  = cv2.FONT_ITALIC
        text = "Width: " + str(cap.get(3)) + "|" + "Height : " + str(cap.get(4))
        time = "time: " + str(datetime.datetime.now()) + text
        # write frames using object
        frame = cv2.putText(frame,time,(50,50),font,1,(25,123,255),1)
        write.write(frame)
        # gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) == ord("z"):
            cv2.destroyAllWindows()
            break
cap.release()
write.release()
cv2.destroyAllWindows()
