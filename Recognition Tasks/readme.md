# Recognition Tasks using Deep Learning (Face Recognition + Emotion Analysis)

## Overview
This project implements a complete face recognition pipeline using deep learning techniques. It covers embedding learning with Siamese Networks, face verification, multi-face recognition, and emotion i.e happiness detection in images. The notebook is divided into multiple stages, progressing from training a model to applying it in real-world scenarios like group photo analysis.

## Objectives
  - Learn face embeddings using Siamese Networks
  - Perform face verification (1:1 matching)
  - Implement face detection using deep learning (OpenCV DNN)
  - Build a face recognition system with a database
  - Extend recognition with emotion analysis (happiness detection)

## Technologies Used
  - Python
  - OpenCV (cv2)
  - NumPy
  - Matplotlib
  - TensorFlow / Keras
  - Scikit-learn
  - DeepFace
  - OpenCV DNN Face Detector

## Workflow Explanation
1. Siamese Network Training (Cell 1): The project begins by building a Siamese Network using a CNN-based embedding model. Uses Labeled Faces in the Wild (LFW) dataset. Preprocesses images to 160×160 resolution. Generates triplets (Anchor, Positive, Negative). Trains using Triplet Loss to learn similarity.
2. Face Verification (Cell 2): This stage performs 1:1 face matching. Extracts embeddings from two images. Computes cosine distance. Applies threshold to decide match.
3. Multi-Face Recognition System (Cell 3): Builds a real-world face recognition pipeline. Detects faces using OpenCV DNN model. Extracts embeddings using a FaceNet-style model. Matches faces against a known database.
4. Emotion Detection (Cell 4): Enhances recognition by adding emotion analysis. Uses DeepFace for emotion prediction. Extracts happiness score (%). Displays identity + emotion together.
5. Final Integrated Recognition (Cell 5): This cell combines Face detection, Recognition, Emotion analysis.

## Input Requirements
  - Dataset (automatically downloaded):
      - LFW Dataset
  - Custom Images:
      - group_photo.jpg
      - group_photo(1).jpg
   
## Applications
  - Face authentication systems
  - Attendance systems
  - Smart surveillance
  - Emotion-aware AI systems
  - Social media image tagging

## Limitations
  - Accuracy depends on training data quality
  - Emotion detection may vary with lighting/pose
  - Requires GPU for faster training (optional)
