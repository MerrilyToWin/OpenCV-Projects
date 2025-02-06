# Face Detection with OpenCV

This repository contains a simple Python script for detecting faces in real-time using OpenCV. The script utilizes Haar Cascade Classifier to identify faces from live video feed captured through the webcam.

## Requirements

- Python 3.x
- OpenCV (`cv2`)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MerrilyToWin/face-detection.git
   cd face-detection
   ```

2. **Install the required libraries:**

   You can install OpenCV using pip:

   ```bash
   pip install opencv-python
   ```

## Usage

1. **Download the Haar Cascade Classifier XML file:**

   Ensure you have the `haarcascade_frontalface_default.xml` file. You can download it from the OpenCV GitHub repository [here](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml).

2. **Run the script:**

   ```bash
   python face_detection.py
   ```

   The script will open a window showing the live feed from your webcam. Faces detected will be highlighted with a blue rectangle.

3. **Exit the script:**

   Press `q` on your keyboard to exit the video feed and close the window.

## Code Explanation

- **Importing Libraries:** The script starts by importing the `cv2` module from OpenCV.
- **Loading Haar Cascade Classifier:** The `CascadeClassifier` object is initialized with the pre-trained Haar Cascade XML file.
- **Capturing Video:** The `VideoCapture` object is used to capture video from the default webcam.
- **Processing Frames:** Each frame is converted to grayscale, and faces are detected using `detectMultiScale`.
- **Drawing Rectangles:** Detected faces are highlighted with rectangles.
- **Displaying Video Feed:** The video feed is displayed in a window. Pressing `q` will exit the loop and close the window.
