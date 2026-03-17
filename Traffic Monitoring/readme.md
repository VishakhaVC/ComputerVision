# Traffic Monitor using YOLOv8 and Vehicle Speed Analysis
## Project Overview
This project is a computer vision-based traffic monitoring system that uses YOLOv8 object detection and tracking to analyze road traffic from a video. The system detects and tracks vehicles, estimates their movement speed using frame-to-frame displacement, counts vehicles on the road, identifies slow-moving traffic, and detects possible traffic congestion. It also generates an output video with live annotations such as vehicle bounding boxes, tracking IDs, estimated speed, vehicle count, slow vehicle count, traffic level, congestion warning.

## Objectives
  - Detect vehicles from traffic video
  - Track each vehicle with a unique ID
  - Estimate vehicle speed using motion between frames
  - Count total vehicles in each frame
  - Identify slow-moving vehicles
  - Classify traffic flow level
  - Detect congestion automatically
  - Save processed traffic video with annotations
    
## Technologies Used
  - Python
  - OpenCV
  - NumPy
  - YOLOv8 (Ultralytics)
  - Matplotlib

## Project Workflow
1. Load Input Files: The project loads input traffic video & YOLOv8 model weights.

2. Vehicle Detection and Tracking: The system uses YOLOv8 tracking to detect and assign IDs to moving vehicles in each frame.

3. Speed Estimation: Vehicle speed is estimated using the pixel displacement of the vehicle center between consecutive frames.

4. Vehicle Memory Management: The system stores tracking-related information in dictionaries like previous positions, speed memory, speed history, last seen frame count. This helps maintain tracking consistency and remove vehicles that disappear for too long.

5. Traffic Analysis: The project calculates i.e total vehicle count, number of slow vehicles, traffic level, congestion state.

6. Visualization: The output frame includes green bounding boxes, vehicle ID labels, estimated speed text, 
traffic statistics, congestion warning.

## Limitations
  - Speed is estimated in pixel units, not real-world km/h
  - Accuracy depends on camera angle and road perspective
  - No lane-wise analysis is included
  - Results may vary with poor lighting or occlusion
  - Congestion thresholds are manually defined
  - The system does not use road calibration for real speed measurement

## Future Improvements
  - Convert pixel speed to real-world speed using calibration
  - Add lane detection
  - Add vehicle counting by direction
  - Use region-based congestion zones
  - Store traffic statistics in CSV file
  - Build dashboard for traffic analytics
  - Add alert system for abnormal traffic conditions
  - Improve performance for real-time deployment
