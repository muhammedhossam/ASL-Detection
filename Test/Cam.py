import os
import time

from ultralytics import YOLO
import cv2
import numpy as np


cap = cv2.VideoCapture(0)

print("we load the model wait . . . !!!")

# model_path = os.path.join('.', 'Train', 'runs', 'detect', 'train', 'weights', 'best.pt')
# load the model
model = YOLO('./best.pt')

# Detection threshold
threshold = 0.5

print("Press 'X' to quit.")

while True:

    ret, frame = cap.read()

    # Run the YOLO model
    results = model(frame)[0]

    # print("the score is ==== ",results)
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result
        if score > threshold:
            # Draw bounding box and label
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

    cv2.imshow('frame1', frame)

    if cv2.waitKey(1) == ord('x'):
        break

cap.release()
cv2.destroyAllWindow()
