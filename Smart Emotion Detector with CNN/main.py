import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from keras.models import load_model
from time import time
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
from keras.models import Sequential
from keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense
from keras.optimizers import Adam
import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier('.\haarcascade_frontalface_default.xml')
classifier =load_model(r'.\model.h5')

emotion_labels = ['Angry','Disgust','Fear','Happy','Neutral', 'Sad', 'Surprise']

cap = cv2.VideoCapture(0)

emotion_timers = {label: 0 for label in emotion_labels}
emotion_display_duration = 30 
last_printed_emotions = set()

model = Sequential()
model.add(Input(shape=(48, 48, 3)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(10, activation='softmax'))


opt = Adam(learning_rate=0.0001)
model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])


while True:
    _, frame = cap.read()
    labels = []
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)



        if np.sum([roi_gray])!=0:
            roi = roi_gray.astype('float')/255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi,axis=0)

            prediction = classifier.predict(roi)[0]
            label=emotion_labels[prediction.argmax()]
            label_position = (x,y)
            cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

            emotion_timers[label] = time()
            detected_emotion = label
        else:
            cv2.putText(frame,'No Faces',(30,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    
    current_time = time()
    for emotion, last_detected in emotion_timers.items():
        if current_time - last_detected > emotion_display_duration:
            if emotion not in last_printed_emotions:
                print(f"Emotion '{emotion}' has been detected for more than {emotion_display_duration} seconds.")
                last_printed_emotions.add(emotion)
        else:
            # Remove the emotion from the printed set if it is no longer detected for the required duration
            if emotion in last_printed_emotions:
                last_printed_emotions.remove(emotion)

    cv2.imshow('Emotion Detector',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




