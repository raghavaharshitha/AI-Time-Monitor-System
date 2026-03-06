import cv2
import time
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

model = YOLO("yolov8n.pt")
tracker = DeepSort()

entry_times = {}

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]
    detections = []

    for box in results.boxes:

        cls = int(box.cls[0])

        if cls == 0:

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])

            detections.append(([x1, y1, x2-x1, y2-y1], conf, "person"))

    tracks = tracker.update_tracks(detections, frame=frame)

    for track in tracks:

        if not track.is_confirmed():
            continue

        track_id = track.track_id
        l, t, r, b = map(int, track.to_ltrb())

        if track_id not in entry_times:
            entry_times[track_id] = time.time()

        elapsed = int(time.time() - entry_times[track_id])

        minutes = elapsed // 60
        seconds = elapsed % 60

        cv2.rectangle(frame, (l, t), (r, b), (0,255,0), 2)

        cv2.putText(frame,
                    f"ID {track_id}",
                    (l, t-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255,0,0),
                    2)

        cv2.putText(frame,
                    f"Time {minutes:02d}:{seconds:02d}",
                    (l, t+20),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0,0,255),
                    2)

    cv2.imshow("Person Time Monitor", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()