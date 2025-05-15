from flask import Flask, request, render_template, Response
import pickle
import cv2
import mediapipe as mp
import pyautogui
import os
import subprocess
import pyttsx3

app = Flask(__name__)

# Model prefetch
model_dict = pickle.load(open('E:/HandGesture/project/computer-Operate/app/model.p', 'rb'))
model = model_dict['model']

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.7)

labels_dict = {0: 'volume-up', 1: 'volume-down', 2: 'open-folder', 3: 'open-notepad'}


def generate_frames():
    last_prediction = None
    engine = pyttsx3.init()

    while True:
        data_aux = []
        x_ = []
        y_ = []

        ret, frame = cap.read()
        H, W, _ = frame.shape
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    x_.append(x)
                    y_.append(y)

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))

            x1 = int(min(x_) * W) - 10
            y1 = int(min(y_) * H) - 10
            x2 = int(max(x_) * W) - 10
            y2 = int(max(y_) * H) - 10

            prediction = model.predict([data_aux])
            predicted_character = labels_dict[int(prediction[0])]

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
            cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3)
            cv2.putText(frame, predicted_character, (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3)

            if predicted_character != last_prediction:
                last_prediction = predicted_character
                engine.say(predicted_character.replace("-", " "))
                engine.runAndWait()

                if predicted_character == 'volume-up':
                    pyautogui.press('volumeup')
                elif predicted_character == 'volume-down':
                    pyautogui.press('volumedown')
                elif predicted_character == 'open-folder':
                    path = './test/'
                    path = os.path.realpath(path)
                    os.startfile(path)
                elif predicted_character == 'open-notepad':
                    subprocess.run(["notepad", "filename.txt"])

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


# routes
@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == '123':
            msg = 'You have successfully logged in'
            return render_template('index.html', msg=msg)
        else:
            msg = 'Please enter correct credentials!'
            return render_template('sign-in.html', msg=msg)
    return render_template('sign-in.html', msg="")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    # app.debug = True
    app.run()
