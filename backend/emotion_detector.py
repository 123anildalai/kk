from deepface import DeepFace
import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
print(result[0]['dominant_emotion'])

cap.release()