import streamlit as st
from google import genai
from dotenv import load_dotenv
import os
from moviepy.video.io.VideoFileClip import VideoFileClip

load_dotenv()
gemini = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

folder_temp = "temp"
file_audio_temp = f"{folder_temp}/audio.mp3"
file_video_temp = f"{folder_temp}/video.mp4" 


def transcribe_audio(file_audio, prompt=None):
    """ Função para transcrever áudios"""
    if file_audio:
        arquivo = gemini.files.upload(
            file=file_audio,
            config={"mime_type": file_audio.type}
            )
        instrucao = prompt or "Gere uma transcrição completa e literal deste áudio, em português."
        response = gemini.models.generate_content(
            model="gemini-3.6-flash",
            contents=[instrucao, arquivo],
        )
        return response.text
    else:
        return None

def transcribe_video(file_video, prompt=None):
    """ Função para transcrever videos"""
    if file_video:
        with open(file_video_temp, "wb") as f_video:
            f_video.write(file_video.read())
        video_convert = VideoFileClip(file_video_temp)
        video_convert.audio.write_audiofile(file_audio_temp)
        with open(file_audio_temp, "rb") as f_audio:
            audio = f_audio.read()
        instrucao = prompt or "Gere uma transcrição completa e literal deste áudio, em português."
        response = gemini.models.generate_content(
            model="gemini-3.6-flash",
            contents=[instrucao, audio],
        )
        return response.text
    else:
        return None

def main():
    """ Função principal da aplicação"""
    st.header("🎙️ App de Transcrição", divider=True)
    st.subheader("Transcreva áudios e videos")
    tabs = ["Vídeo", "Áudio"]
    tab_video, tab_audio = st.tabs(tabs)
    with tab_video:
        st.markdown("Teste em vídeo")
        prompt_video = st.text_input("Digite o prompt: ", key="prompt_video")
        file_video = st.file_uploader("Selecione um video", type=["mp4", "mov", "avi"])
        if file_video:
            transcricao_video = transcribe_video(file_video, prompt_video)
            if transcribe_video:
                st.write(transcricao_video)
            else:
                st.error("Erro ao transcrever o vídeo")
    with tab_audio:
        st.markdown("Teste em áudio")
        prompt_audio = st.text_input("Digite o prompt: ", key="prompt_audio")
        file_audio = st.file_uploader("Selecione um áudio", type=["mp3", "wav", "ogg"])
        if file_audio:
            transcicao_audio = transcribe_audio(file_audio, prompt_audio)
            if transcicao_audio:
                st.write(transcicao_audio)
            else:
                st.error("Erro ao transcrever o áudio")




if __name__ == "__main__":
    main()