import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
gemini = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def main():
    """ Função principal da aplicação"""
    st.header("🎙️ App de Transcrição", divider=True)
    st.subheader("Transcreva áudios e videos")
    tabs = ["Vídeo", "Áudio"]
    tab_video, tab_audio = st.tabs(tabs)
    with tab_video:
        st.markdown("Teste em vídeo")
    with tab_audio:
        st.markdown("Teste em áudio")
        prompt_audio = st.text_input("Digite o prompt: ")
        file_audio = st.file_uploader("Selecione um áudio", type=["mp3", "wav", "ogg"])
        if file_audio:
            transcicao_audio = transcribe_audio(file_audio, prompt_audio)
            if transcicao_audio:
                st.write(transcicao_audio)
            else:
                st.error("Erro ao transcrever o áudio")

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

if __name__ == "__main__":
    main()