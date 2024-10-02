from ultralytics import YOLO
import cv2


model = YOLO(r"Users\shiva\Desktop\python projects\object detection\yolov8n.pt")

def object():
    cap = cv2.VideoCapture(0)
    width = 1280
    height = 720
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    ret, frame = cap.read()

    if ret:
        results = model.track(frame, persist=True)
        frame_ = results[0].plot()
        cv2.imshow('frame', frame_)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cap.release()
