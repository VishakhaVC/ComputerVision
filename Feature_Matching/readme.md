# Feature Matching using SIFT, ORB, SURF and BFMatcher
## Project Overview

This project demonstrates feature detection, descriptor extraction, and feature matching between two images using classical computer vision techniques in OpenCV.

The project uses:
  SIFT for scale-invariant feature detection
  ORB for fast binary feature detection
  SURF as an optional detector if available
  BFMatcher with Lowe’s Ratio Test for reliable feature matching

The implementation is useful for understanding how local features are detected and matched across different images.

## Objectives
  - Load and preprocess images
  - Detect keypoints in images
  - Compute descriptors using SIFT, ORB, and SURF
  - Visualize detected keypoints
  - Match features between two images
  - Apply BFMatcher
  - Filter matches using Lowe’s Ratio Test
  - Visualize good matches between two images

## Technologies Used
  - Python
  - OpenCV
  - NumPy
  - Matplotlib

## Project Workflow
### Part 1: Feature Detection
  1. Load input image
  2. Convert image to grayscale
  3. Detect keypoints using:
       - SIFT
       - ORB
       - SURF
  4. Compute descriptors for each keypoint
  5. Draw and display keypoints on the original image

### Part 2: Feature Matching
  1. Load two images
  2. Compute SIFT keypoints and descriptors for both images
  3. Use BFMatcher with knnMatch()
  4. Select 2 nearest matches for each descriptor
  5. Apply Lowe’s Ratio Test
  6. Keep only strong matches
  7. Visualize the final matched keypoints between both images

## Algorithms Used
1. SIFT (Scale-Invariant Feature Transform) detects stable keypoints and computes descriptors that are robust to scale changes, rotation, illumination changes. It is highly accurate and widely used for feature matching.

2. ORB (Oriented FAST and Rotated BRIEF) is a faster alternative to SIFT. It is computationally efficient, suitable for real-time applications, based on binary descriptors.

3. SURF (Speeded-Up Robust Features) is another feature detector and descriptor. It is faster than SIFT in some cases, but it may not be available in all OpenCV builds because it belongs to the non-free/patented module.

4. BFMatcher (Brute Force Matcher) compares descriptors of one image with descriptors of another image and finds the closest matches. 

5. Lowe’s Ratio Test helps remove weak or ambiguous matches. For each descriptor: find the 2 nearest matches & accept the best match only if: m.distance < 0.75 × n.distance. This improves the quality of final feature matches.

## Applications
  - Image stitching
  - Object recognition
  - Panorama creation
  - Visual localization
  - 3D reconstruction
  - Motion tracking
  - Augmented reality

## Limitations
  - Matching quality depends on image texture and viewpoint changes
  - SURF may not run in standard OpenCV installations
  - BFMatcher can be slower for large descriptor sets
  - Repetitive patterns may create false matches
  - SIFT and SURF are computationally heavier than ORB

## Future Improvements
  - Add ORB matching with Hamming distance
  - Compare SIFT vs ORB matching performance
  - Estimate homography between matched images
  - Add RANSAC for outlier rejection
  - Extend project to image stitching
  - Test on real-world images beyond chessboard patterns
