import streamlit as st
import speech_recognition as sr
from io import BytesIO

# Configure the Streamlit app
st.title("Real-Time Speech-to-Text Application")
st.write("Use your microphone to transcribe speech in real-time.")

# Language selection
language_options = {
    "English": "en-US",
    "Russian": "ru-RU",
    "Uzbek": "uz-UZ"
}
selected_language = st.selectbox("Select a language for transcription:", options=list(language_options.keys()))

# Initialize the recognizer
recognizer = sr.Recognizer()

# Start microphone recording
if st.button("Start Recording"):
    st.write("Listening... Speak into the microphone.")
    with sr.Microphone() as source:
        try:
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=10)  # Listen for up to 10 seconds
            
            # Transcribe speech
            st.write("Processing...")
            transcription = recognizer.recognize_google(audio, language=language_options[selected_language])
            st.success(f"Transcription: {transcription}")
        except sr.UnknownValueError:
            st.error("Sorry, could not understand the audio.")
        except sr.RequestError as e:
            st.error(f"Could not request results from Google Speech Recognition service; {e}")
