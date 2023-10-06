import numpy as np
import tensorflow as tf
import cv2
import signal


class FacialExpressionModel(object):
    EMOTIONS_LIST = ["Angry", "Disgust",
                     "Fear", "Happy",
                     "Neutral", "Sad",
                     "Surprise"]

    # def __init__(self, emotion_model):
    #     self.emotion_model = emotion_model

    def __init__(self, model_path):
        self.model_path = model_path
        self.emotion_model = None
        self.emotion_counts = {emotion: 0 for emotion in FacialExpressionModel.EMOTIONS_LIST}
        self.load_model()

    def load_model(self):
        try:
            self.emotion_model = tf.keras.models.load_model(self.model_path)
            print("Loaded emotion detection model.")
        except Exception as e:
            print(f"Error loading emotion detection model: {str(e)}")

    def predict_emotion(self, img):
        if self.emotion_model is not None:
            preds = self.emotion_model.predict(img)
            emotion = FacialExpressionModel.EMOTIONS_LIST[np.argmax(preds)]
            self.emotion_counts[emotion] += 1
            return emotion
        else:
            return "Model not loaded"

    # def predict_emotion(self, img):
    #     self.preds = self.emotion_model.predict(img)
    #     return FacialExpressionModel.EMOTIONS_LIST[np.argmax(self.preds)]


facec = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
model_path = FacialExpressionModel('emotionModel.h5')
font = cv2.FONT_HERSHEY_SIMPLEX


class VideoCamera(object):
    def __init__(self, path):
        self.video = cv2.VideoCapture(path)
        self.frame_count = 0
        self.total_frames = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))
        self.threshold_frame = int(self.total_frames * 3 / 4)

    def __del__(self):
        self.video.release()

    # returns camera frames along with bounding boxes and predictions
    def get_frame(self):

        _, fr = self.video.read()
        self.frame_count += 1
        gray_fr = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
        faces = facec.detectMultiScale(gray_fr, 1.3, 5)
        for (x, y, w, h) in faces:
            fc = gray_fr[y:y + h, x:x + w]
            roi = cv2.resize(fc, (48, 48))
            pred = model_path.predict_emotion(roi[np.newaxis, :, :, np.newaxis])

            # Draw bounding box
            cv2.rectangle(fr, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Add label with prediction
            cv2.putText(fr, f'Emotion: {pred}', (x, y - 10), font, 0.9, (255, 255, 0), 2)

            # Print the detected emotion in the terminal
            print(f'Detected Emotion: {pred}')

            # Count emotions after reaching the threshold frame
            if self.frame_count >= self.threshold_frame:
                self.count_emotions()

        return fr

    def count_emotions(self):
        try:
            with open('emotion_counts.txt', 'w') as file:
                for emotion, count in model_path.emotion_counts.items():
                    file.write(f'{emotion}: {count}\n')
        except KeyboardInterrupt:
            with open('emotion_counts.txt', 'w') as file:
                for emotion, count in model_path.emotion_counts.items():
                    file.write(f'{emotion}: {count}\n')


def gen(camera):
    while True:
        frame = camera.get_frame()
        cv2.imshow('Facial Expression Reorganization', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


def save_emotion_counts():
    with open('emotion_counts.txt', 'w') as file:
        for emotion, count in model_path.emotion_counts.items():
            file.write(f'{emotion}: {count}\n')


# Create a VideoCamera instance with the path to your video file
camera = VideoCamera('FaceRecon.mp4')

# Call the 'gen' function to start the facial expression recognition
gen(camera)


