import cv2
from ultralytics import YOLO

# Load the YOLO model
model = YOLO('best.pt')

# Input video file path
input_video = 'IMG_0270.mp4'

# Output video file path
output_video = 'output_video.mp4'

# Open the video file
cap = cv2.VideoCapture(input_video)

# Get the video properties (width, height, and fps)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Create VideoWriter object to save the processed frames to a new video file
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for mp4 file format
out = cv2.VideoWriter(output_video, fourcc, fps, (frame_width, frame_height))

# Process video frames without displaying them
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection on the frame with verbose=False to suppress logs
    results = model(frame, verbose=False)  # Suppress logging here

    # Annotate the frame with bounding boxes and labels
    annotated_frame = results[0].plot()  # The plot method draws the bounding boxes

    # Write the annotated frame to the output video file
    out.write(annotated_frame)

# Release resources
cap.release()
out.release()

print(f"Processed video saved to {output_video}")
