import os
import cv2
import numpy as np
import mediapipe as mp
from tensorflow.keras.models import load_model

# المسار الكامل للنموذج
model_path = '/Users/mac/Documents/Library/assets/pages/age_model.h5'

# التحقق من وجود النموذج قبل تحميله
if os.path.exists(model_path):
    model = load_model(model_path)
else:
    raise FileNotFoundError(f"Model file not found: {model_path}")

# إعداد MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# دالة لتجهيز صورة الوجه قبل إرسالها للموديل
def preprocess_face(face_img):
    face_img = cv2.resize(face_img, (100, 100))
    face_img = face_img / 255.0
    face_img = np.expand_dims(face_img, axis=0)
    return face_img

# فتح الكاميرا
cap = cv2.VideoCapture(0)

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.6) as face_detection:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # قلب الصورة علشان تكون شبه المرايا
        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape

        # تحويل الصورة لـ RGB لأن MediaPipe بيشتغل بـ RGB
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(img_rgb)

        if results.detections:
            for detection in results.detections:
                # استخراج مكان الوجه
                bboxC = detection.location_data.relative_bounding_box
                x, y, w_box, h_box = bboxC.xmin, bboxC.ymin, bboxC.width, bboxC.height
                x, y, w_box, h_box = int(x * w), int(y * h), int(w_box * w), int(h_box * h)

                # قص الوجه من الصورة
                face_img = frame[y:y+h_box, x:x+w_box]
                if face_img.shape[0] > 0 and face_img.shape[1] > 0:
                    input_face = preprocess_face(face_img)
                    predicted_age = model.predict(input_face)[0][0]

                    # رسم البوكس والعمر
                    cv2.rectangle(frame, (x, y), (x+w_box, y+h_box), (0, 255, 0), 2)
                    cv2.putText(frame, f"Age: {int(predicted_age)}", (x, y-10), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        cv2.imshow("Age Estimation - Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
