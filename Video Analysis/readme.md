# Sports Video Analysis using YOLOv8 Player Tracking
## Project Overview
This project is a sports video analysis system built using YOLOv8 and OpenCV. It detects and tracks players in a sports video, assigns each detected player a unique ID, and visualizes their movement path across frames. The system focuses on person detection and tracks player motion over time, making it useful for basic sports analytics and movement analysis.

## Objectives
  - Detect players in a sports video
  - Track each player across frames
  - Assign unique tracking IDs
  - Count the number of players visible in each frame
  - Visualize player movement using trails
  - Display annotated video frames inside Jupyter Notebook

## Technologies Used
  - Python
  - OpenCV
  - NumPy
  - YOLOv8 (Ultralytics)
  - Matplotlib

## Main Logic
1. Player Detection: YOLOv8 detects all objects in the frame.
2. Person Filtering: Only objects with class ID 0 are treated as players.
3. Tracking: The track() function assigns IDs to detected players and keeps them consistent across frames.
4. Path Storage: The center point of each player’s bounding box is saved over time to create movement trails.
5. Visualization: The output frame shows player rectangles, player labels, player count, trajectory lines.

## Visualization Details
  - Green boxes -> detected players
  - Green text -> player ID
  - Blue lines -> movement paths
  - Yellow text -> player count

## Applications
  - Sports analytics
  - Player movement analysis
  - Match performance visualization
  - Tactical analysis
  - Training review
  - Athlete tracking research

## Limitations
  - Only tracks the person class, not ball or specific team identity
  - No player re-identification if tracking is lost
  - No speed or distance calculation
  - No event analysis such as passes, goals, or possession
  - Tracking quality depends on video quality and camera angle

## Future Improvements
  - Add ball detection and tracking
  - Calculate player speed and distance covered
  - Separate players by team colors
  - Add heatmap generation for player movement
  - Detect key events such as passes or shots
  - Export analytics data to CSV
  - Save processed video output
