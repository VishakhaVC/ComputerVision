# Face and Eye Detection using OpenCV

# Project Overview
This project implements a basic computer vision application that detects human faces and eyes in an image using Haar Cascade classifiers with the OpenCV library. The program loads an image, detects faces in the image, and then detects eyes within the detected face regions. Rectangles are drawn around faces and circles are drawn around eyes to visualize the detections. This project demonstrates the use of classical computer vision techniques for object detection.

# Objective
  - Detect human faces from an image
  - Detect eyes inside detected faces
  - Visualize detections using bounding boxes and circles
  - Understand the use of Haar Cascade classifiers in OpenCV

# Technologies Used
  - Python
  - OpenCV (cv2)
  - NumPy
  - Haar Cascade Classifiers

# Project Workflow
  - Load the input image using OpenCV.
  - Convert the image to grayscale for efficient processing.
  - Load pre-trained Haar Cascade classifiers for face and eye detection.
  - Detect faces in the image using the face cascade.
  - Draw rectangles around detected faces.
  - Define the Region of Interest (ROI) for each detected face.
  - Detect eyes within the face region.
  - Draw circles around detected eyes.
  - Display the final output image with detections.

# Sample Output
  - Faces will be highlighted with blue rectangles.
  - Eyes will be marked with green circles.

# Applications
  - Face recognition systems
  - Surveillance systems
  - Human-computer interaction
  - Security systems
  - Attendance monitoring

# Limitations
  - Works best with frontal faces
  - Performance may decrease with low lighting or occlusions
  - Haar Cascade is less accurate compared to deep learning based detectors
