**Emotion Detection System**
**Overview**
This project is an emotion detection system that identifies human emotions from facial expressions in images or video streams. The system uses a combination of Haar Cascade classifiers for face detection and a Convolutional Neural Network (CNN) model for emotion classification.

## Features
- **Face Detection**: Uses Haar Cascade classifier to detect faces in real-time.
- **Emotion Classification**: Classifies emotions into categories like Angry, Happy, Sad, etc., using a pre-trained CNN model.
- **Real-Time Processing**: Capable of processing video streams from a webcam.

## Project Structure
- `haarcascade_frontalface_default.xml`: Pre-trained Haar Cascade classifier for face detection.
- `model.h5`: Pre-trained CNN model for emotion classification.
- `main.py`: Main script that integrates face detection and emotion classification.
- `emotion-detector-3.ipynb`: Jupyter notebook for model training and testing.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/emotion-detection.git
    ```
2. Navigate to the project directory:
    ```bash
    cd emotion-detection
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the `main.py` script to start the emotion detection:
    ```bash
    python main.py
    ```

2. Press `q` to exit the application.

## Requirements

- Python 3.x
- OpenCV
- TensorFlow/Keras
- Numpy

## Model Training (Optional)
If you wish to train your own model, use the `emotion-detector-3.ipynb` notebook. Ensure you have a dataset of labeled facial expressions.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- The pre-trained Haar Cascade model provided by OpenCV.
- The dataset used for training the CNN model.
