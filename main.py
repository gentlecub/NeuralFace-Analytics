import cv2
import numpy as np
from tensorflow.keras.models import load_model

model_path_emotion = "emotion/models/lenet.keras"
model_emotion = load_model(model_path_emotion)

model_path_gender = "gender/models/lenet.keras"
model_gender = load_model(model_path_gender)

model_path_age = "age/models/lenet.keras"
model_age = load_model(model_path_age)

classNames = ["Angry", "Disgust", "Fear", "Happy", "Neutral", "Sad", "Surprise"]
classAgeName =[ "1-2 years",  "3-9 years",  "10-20 years",  "21-27 years",  "28-45 years",  "46-65 years",  "66+ years"]  

def faceBox(faceNet,frame):
    frameHeight = frame.shape[0]
    frameWidth = frame.shape[1]
    blob = cv2.dnn.blobFromImage(frame,1.0, (227,227), [104,117,123], swapRB=False)
    faceNet.setInput(blob)
    detection = faceNet.forward()
    bbox = []
    for i in range(detection.shape[2]):
      confidence = detection[0,0,i,2]
      if confidence >0.7:
        x1 = int(detection[0,0,i,3]*frameWidth)
        y1 = int(detection[0,0,i,4]*frameHeight)
        x2 = int(detection[0,0,i,5]*frameWidth)
        y2 = int(detection[0,0,i,6]*frameHeight)
        bbox.append([x1,y1,x2,y2])
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0), 1)
    return frame,bbox

faceProto = "opencv_face_detector.pbtxt"
faceModel = "opencv_face_detector_uint8.pb"

faceNet = cv2.dnn.readNet(faceModel,faceProto)
MODEL_MEAN_VALUES =(78.4263377603, 87.7689143744, 114.895847746)
gender = ["Male", "Female"]

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Detectar caras y obtener los bounding boxes
    frame, bboxs = faceBox(faceNet, frame)

    for bbox in bboxs:
        cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (255, 0, 0), 2)
        face = frame[bbox[1]:bbox[3], bbox[0]:bbox[2]]
        
        # Procesar la emoción
        face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)  # Convertir a escala de grises
        face_resized = cv2.resize(face_gray, (48, 48))  # Redimensionar a 48x48
        face_resized = face_resized.reshape(1, 48, 48, 1)  # Agregar dimensión para batch y canal
        face_resized = face_resized / 255.0  # Normalizar

        try:
            # Hacer predicción de emoción
            face_predictions = model_emotion.predict(face_resized, verbose=2)
            a = classNames[np.argmax(face_predictions[0])]
        except Exception as e:
            print(f"Error al predecir la emoción: {e}")
            a = "Error"

        # Procesar el género
        gender_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)  # Convertir a escala de grises
        gender_resized = cv2.resize(gender_gray, (100, 100))  # Redimensionar a 100x100
        gender_resized = gender_resized.reshape(1, 100, 100, 1)  # Agregar dimensión para batch y canal
        gender_resized = gender_resized / 255.0  # Normalizar

        try:
            # Hacer predicción de género
            gender_predictions = model_gender.predict(gender_resized, verbose=2)
            b = gender[np.argmax(gender_predictions[0])]
        except Exception as e:
            print(f"Error al predecir el género: {e}")
            b = "Error"
        # Procesar el género
        age_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)  # Convertir a escala de grises
        age_resized = cv2.resize(age_gray, (100, 100))  # Redimensionar a 100x100
        age_resized = age_resized.reshape(1, 100, 100, 1)  # Agregar dimensión para batch y canal
        age_resized = age_resized / 255.0  # Normalizar

        try:
            # Hacer predicción de género
            age_predictions = model_age.predict(age_resized, verbose=2)
            c = classAgeName[np.argmax(age_predictions[0])]
        except Exception as e:
            print(f"Error al predecir el género: {e}")
            c = "Error"

        # Añadir texto en el cuadro de la cara
        label = "{} {} {}".format(a, b, c)
        cv2.putText(frame, label, (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

    # Mostrar el frame con los resultados
    cv2.imshow("Emotion Detection", frame)

    # Presionar 'q' para salir
    k = cv2.waitKey(1)
    if k == ord('q'):
        break