import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    results = model(frame)

    for r in results:
        for box in r.boxes:

            cls = int(box.cls[0])

            if cls == 0:  # person

                x1,y1,x2,y2 = map(int,box.xyxy[0])

                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)

                cv2.putText(frame,"Person",(x1,y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6,(0,255,0),2)

    cv2.imshow("Person Detection",frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()