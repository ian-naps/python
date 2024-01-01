import cv2


cap = cv2.VideoCapture(0)  # Assuming your webcam is device 0

# Example using a Haar cascade classifier for face detection:

face_cascade = cv2.CascadeClassifier('C:\\Users\\ian\\OneDrive\\Documents\\python\\haarcascade_frontalface_default.xml')

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Apply object detection using the loaded model
    detected_objects = face_cascade.detectMultiScale(frame, 1.1, 4)

    # Draw rectangles around detected objects
    for (x, y, w, h) in detected_objects:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the processed frame
    cv2.imshow('Webcam Object Detection', frame)

    # Exit if the 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()


