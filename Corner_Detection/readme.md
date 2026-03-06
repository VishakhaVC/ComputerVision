# Harris and FAST Corner Detection
# Rotation Invariance and Multi-Scale Feature Detection (Computer Vision)

# Project Overview
This project demonstrates corner detection techniques in computer vision using two popular algorithms:
  - Harris Corner Detector
  - FAST (Features from Accelerated Segment Test)
The project analyzes how feature detectors behave under image rotation and different image scales.

# Experiment 1: Corner Detection with Rotation
Objective: To test how well Harris and FAST detectors perform when the image is rotated.
Process:
  1. Load the input image (chess_board.png)
  2. Convert the image to grayscale
  3. Apply Gaussian blur to reduce noise
  4. Detect corners using:
       - Harris detector
       - FAST detector
  5. Rotate the image by 45 degrees
  6. Detect corners again on the rotated image
  7. Visualize the results

# Experiment 2: Multi-Scale Corner Detection
Objective: To analyze how corner detectors behave at different image scales. This is done using a multi-scale pyramid approach, where the image is repeatedly resized and analyzed.

Process:
  1. Load grayscale image
  2. Detect corners using Harris and FAST
  3. Downsample the image
  4. Repeat detection across multiple levels
  5. Map detected corners back to original image coordinates
  6. Draw circles representing scale of detection.

# Key Concepts
  - Gradient Computation: Used to detect intensity change in images.
  - Structure Tensor: Used in Harris detection to measure directional intensity variation.
  - Non-Maximum Suppression (NMS): Removes nearby weak detections and keeps only the strongest corners.
  - Rotation Invariance: Testing whether detected corners remain meaningful after image rotation.
  - Multi-Scale Detection: Detecting features at multiple resolutions to improve robustness.

# Technologies Used
  - Python
  - OpenCV
  - NumPy
  - SciPy
  - Matplotlib

# Applications
Corner detection is widely used in:
  - Image matching
  - Object detection
  - Feature tracking
  - SLAM (Simultaneous Localization and Mapping)
  - Augmented Reality
  - Image stitching
  - Robotics navigation

# Key Learnings
  - Harris detects strong structural corners
  - FAST is much faster and suitable for real-time applications
  - Rotation affects corner positions but features remain detectable
  - Multi-scale analysis improves feature robustness
  - Non-maximum suppression is important to remove redundant detections
