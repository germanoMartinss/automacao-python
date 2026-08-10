import cv2 
import mediapipe as mp
import subprocess
import pyautogui
import os

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

camera = cv2.VideoCapture(0)
resolution_x = 1280
resolution_y = 720 
camera.set(cv2.CAP_PROP_FRAME_WIDTH, resolution_x)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution_y)

vlc_process = None
vlc_patch = "vlc"
music_path = "music/ConeCrewDiretoria - Chefe de Quadrilha.mp3"

gesto_saida = 0
FRAMES_CONFIRMACAO = 5 # Quantidade de frames para confirmar o gesto

GESTO_SAIDA = [True, False, False, True]
GESTO_FECHAR = [False, False, False, False]

PROGRAMAS_POR_GESTO = {
    (True, False, False, False): ["flatpak", "run", "com.google.Chrome"],
    (True, True, False, False): ["flatpak", "run", "com.spotify.Client"],
    (True, True, False, True): ["vlc", music_path],
}


hands = mp_hands.Hands()



def find_coord_hand(img, side_inverted = False):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    all_hands = []
    if results.multi_hand_landmarks:
        for hand_side, hand_landmarks in zip(results.multi_handedness, results.multi_hand_landmarks):
            hand_info = {}
            coords = []
            for mark in hand_landmarks.landmark:
                x = int(mark.x * resolution_x)
                y = int(mark.y * resolution_y)
                z = int(mark.z * resolution_x)
                coords.append((x, y, z))
            hand_info["coordenadas"] = coords

            lado = hand_side.classification[0].label
            if side_inverted:
                lado = "Left" if lado == "Right" else "Right"
            hand_info["lado"] = lado

            all_hands.append(hand_info)
            mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    return img, all_hands

def fingers_raised(hand):
    fingers = []
    for fingertip in [8, 12, 16, 20]:  # Índices dos pontos das pontas dos dedos
        if hand["coordenadas"][fingertip][1] < hand["coordenadas"][fingertip - 2][1]:  # Compara a posição y da ponta do dedo com a posição y da articulação anterior
            fingers.append(True)  # Dedo levantado
        else:
            fingers.append(False)  # Dedo abaixado
    return fingers 

def start_program(comando):
    env = os.environ.copy()
    env.pop("QT_QPA_PLATFORM_PLUGIN_PATH", None)
    env.pop("QT_PLUGIN_PATH", None)
    return subprocess.Popen(comando, env=env)


def close_program(processo):
    if processo is not None:
        processo.terminate()
    return None


def handle_gesture(info_finger_hand, processos_abertos):
    """Abre/fecha o programa correspondente ao gesto atual."""
    comando = PROGRAMAS_POR_GESTO.get(tuple(info_finger_hand))

    if comando is not None:
        chave = comando[-1]  # último item: app-id do flatpak, ou caminho da música pro vlc
        if chave not in processos_abertos:
            processos_abertos[chave] = start_program(comando)
    elif info_finger_hand == GESTO_FECHAR:
        for chave, processo in list(processos_abertos.items()):
            processo.terminate()
        processos_abertos.clear()

    return processos_abertos


def is_gesto_saida_confirmado(info_finger_hand, contador_atual):
    if info_finger_hand == GESTO_SAIDA:
        return contador_atual + 1
    return 0


def main():
    global gesto_saida
    processos_abertos = {}

    while camera.isOpened():
        ret, frame = camera.read()
        if not ret:
            print("Frame vazio da Câmera. Saindo...")
            continue
        frame = cv2.flip(frame, 1)  # Inverte a imagem

        img, all_hands = find_coord_hand(frame)
        if len(all_hands) == 1:
            info_finger_hand = fingers_raised(all_hands[0])
            print(info_finger_hand)

            gesto_saida = is_gesto_saida_confirmado(info_finger_hand, gesto_saida)
            if gesto_saida >= FRAMES_CONFIRMACAO:
                break

            processos_abertos = handle_gesture(info_finger_hand, processos_abertos)

        cv2.imshow("Webcam", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    for processo in processos_abertos.values():
        close_program(processo)
    camera.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1)


def send_keypress(key): 
    pyautogui.press(key)


if __name__ == "__main__":
    main()