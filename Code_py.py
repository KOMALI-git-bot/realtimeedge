import cv2

# Step 1: Initialize webcam capture
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video source.")
    exit()

# Step 2: Process video frames in a loop
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply Canny edge detection
    edges = cv2.Canny(gray_frame, 100, 200)
    
    # Step 3: Display the original and edge-detected frames
    cv2.imshow('Original Video', frame)
    cv2.imshow('Edge-Detected Video', edges)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
