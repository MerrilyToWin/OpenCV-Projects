# Drowsiness and Blink Detection

This repository contains a Python script for real-time detection of drowsiness and blinking using OpenCV and dlib. The script uses a webcam to monitor eye blinks and determine whether the user is active, drowsy, or asleep.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy
- dlib
- imutils

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MerrilyToWin/drowsiness-detection.git
   cd drowsiness-detection
   ```

2. **Install the required libraries:**

   You can install the necessary libraries using pip:

   ```bash
   pip install opencv-python numpy dlib imutils
   ```

3. **Download the dlib shape predictor model:**

   You need to download the `shape_predictor_68_face_landmarks.dat` file, which is used for facial landmark detection. You can download it from [here](https://github.com/davisking/dlib-models).

## Usage

1. **Run the script:**

   ```bash
   python drowsiness_detection.py
   ```

   The script will open a window showing the live feed from your webcam. It will detect faces, monitor eye blinks, and display the user's status as "Active", "Drowsy", or "Sleeping". Notifications will be triggered based on the user's drowsiness count.

2. **Exit the script:**

   Press `q` on your keyboard to stop the video feed and close the window.

## Code Explanation

- **Importing Libraries:** The script imports necessary libraries including OpenCV, NumPy, dlib, and imutils.
- **Initializing Detectors:** The `dlib` face detector and landmark predictor are initialized.
- **Blink Detection:** The script calculates the blink ratio to determine if the eyes are blinking.
- **Status Tracking:** Based on eye blinks, the script tracks the user's status (active, drowsy, or asleep) and updates the status message.
- **Notification Logic:** The script prints notifications based on the number of detected drowsy states.
- **Display:** The video feed is displayed with annotations for the user's status.

## Acknowledgments

- OpenCV for video and image processing.
- dlib for facial landmark detection.
- [dlib Models Repository](https://github.com/davisking/dlib-models) for the pre-trained shape predictor.
