import cv2
import mediapipe as mp
import numpy as np
import time

mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh

p_left_eye = [385, 380, 387, 373, 362, 263]
p_right_eye = [160, 144, 158, 153, 33, 133]
p_eyes = p_left_eye + p_right_eye

threshold_eye = 0.3
closed_eyes = 0

def calculate_ear(face, p_right_eye, p_left_eye):
    try:
        face = np.array([[coord.x, coord.y] for coord in face])
        face_left = face[p_left_eye, :]
        face_right = face[p_right_eye, :]
        ear_left = (np.linalg.norm(face_left[0]-face_left[1]) + np.linalg.norm(face_left[2]-face_left[3])) / (2*(np.linalg.norm(face_left[4]-face_left[5])))
        ear_right = (np.linalg.norm(face_right[0]-face_right[1]) + np.linalg.norm(face_right[2]-face_right[3])) / (2*(np.linalg.norm(face_right[4]-face_right[5])))
    except:
        ear_left = 0.0
        ear_right = 0.0
    ear_mean = (ear_left + ear_right) / 2
    return ear_mean

camera = cv2.VideoCapture(0)

with mp_face_mesh.FaceMesh(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as face_mesh:
    while camera.isOpened():
        ret, frame = camera.read()
        if not ret:
            print("Frame vazio da Câmera. Saindo...")
            continue

        length, width, _ = frame.shape
        # Transforma BGR para RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_mesh_output = face_mesh.process(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        if face_mesh_output.multi_face_landmarks:
            for face_landmarks in face_mesh_output.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    face_landmarks,
                    mp_face_mesh.FACEMESH_CONTOURS,
                    mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
                    mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=1, circle_radius=1)
                )
                face = face_landmarks.landmark
                for id_coord, coord_xyz in enumerate(face):
                    if id_coord in p_eyes:
                        coord_cv = mp_drawing._normalized_to_pixel_coordinates(
                            coord_xyz.x,
                            coord_xyz.y,
                            width,
                            length
                        )
                        cv2.circle(frame, coord_cv, 2, (255, 0, 0), -1)
                        ear = calculate_ear(face, p_right_eye, p_left_eye)
                        cv2.rectangle(frame, (0, 1), (250, 120), (0, 0, 0), -1)
                        cv2.putText(frame, f"EAR: {round(ear, 2)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                        if ear < threshold_eye:
                            t_initial = time.time() if closed_eyes == 0 else t_initial
                            closed_eyes = 1
                        if closed_eyes == 1 and ear > threshold_eye:
                            closed_eyes = 0
                        t_final = time.time()

                        tempo = (t_final - t_initial) if closed_eyes == 1 else 0.0
                        cv2.putText(frame, f"Tempo: {round(tempo, 3)}", (1, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                        if tempo >= 2.0:
                            cv2.rectangle(frame, (30, 350), (600, 430), (100, 200, 200), -1)
                            cv2.putText(frame, f"Muito tempo de olho fechado!", (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow("Webcam", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

camera.release()
cv2.destroyAllWindows()
cv2.waitKey(1)
