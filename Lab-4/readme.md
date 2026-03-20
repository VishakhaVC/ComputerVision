# Medical Image Analysis Using CNN

## Project Overview
This project implements a deep learning-based system to analyze mammography images and classify them into three categories: Normal, Benign, and Malignant. The model leverages Convolutional Neural Networks (CNNs) with transfer learning to achieve high accuracy on medical image data. The goal is to assist in early detection of breast cancer by automating image classification.

## Features
  - Automatic dataset download using KaggleHub
  - Image preprocessing and augmentation
  - Handling class imbalance using class weights
  - Transfer learning using a pretrained CNN
  - Model training with early stopping and checkpointing
  - Performance visualization (Accuracy & AUC)
  - Single image prediction with confidence score

## Technologies Used
  - Python
  - TensorFlow / Keras
  - OpenCV
  - NumPy
  - Matplotlib
  - Scikit-learn

## Workflow
1. Dataset Download:The dataset is automatically downloaded and extracted using KaggleHub.
2. Data Preprocessing: Resize images to 224×224, Normalize pixel values, Split into training and validation sets.
3. Data Augmentation: Rotation, Horizontal flipping, Zoom.
4. Class Balancing: Class weights are calculated to handle imbalance in dataset distribution.
5. Model Training:
   - Optimizer: Adam
   - Loss: Categorical Crossentropy
   - Metrics: Accuracy, AUC
   - Callbacks:
      - EarlyStopping
      - ModelCheckpoint
6. Evaluation: Training and validation performance is visualized using Accuracy graph & AUC-ROC graph.
7. Prediction: The model can predict a single image and output. Predicted class, Confidence score, Visualization of result.

## Future Improvements
  - Fine-tune the base model for better accuracy
  - Add Grad-CAM for model explainability
  - Deploy as a web application
  - Use larger medical datasets
