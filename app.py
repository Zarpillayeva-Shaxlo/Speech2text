import streamlit as st
import whisper
import sounddevice as sd
from scipy.io.wavfile import write
import os

# Streamlit sarlavha
st.title("Speech-to-Text (STT) Web App")
st.write("Ovozli matnni yozib olish va matnga aylantiruvchi veb-dastur.")

# Til tanlash
language = st.selectbox("Tilni tanlang:", ("Inglizcha", "Ruscha", "O'zbekcha"))

# Whisper uchun til kodi
lang_code = {"Inglizcha": "en", "Ruscha": "ru", "O'zbekcha": "uz"}

# Modelni yuklash
@st.cache_resource
def load_model():
    return whisper.load_model("base")

model = load_model()

# Audio yozib olish
if st.button("Ovoz yozib olish va matnga aylantirish"):
    st.write("Ovoz yozib olinmoqda... 5 soniya davomida gapiring.")
    duration = 5  # Recording duration in seconds
    fs = 44100  # Sample rate

    try:
        # Ovoz yozish
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()
        audio_file = "recorded_audio.wav"
        write(audio_file, fs, recording)

        # Matnga aylantirish
        st.write("Matnga aylantirilmoqda...")
        result = model.transcribe(audio_file, language=lang_code[language])
        st.success("Matn muvaffaqiyatli tanildi!")
        st.text_area("Taniqli matn:", result['text'])

        # Yozib olingan audio faylni o'chirish
        os.remove(audio_file)
    except Exception as e:
        st.error(f"Xatolik yuz berdi: {e}")


# import streamlit as st
# import speech_recognition as sr

# # Streamlit sarlavha
# st.title("Multilingual Speech-to-Text (STT) Web App")
# st.write("Ovozli matnni yozib olish va matnga aylantiruvchi veb-dastur (Inglizcha, Ruscha, O'zbekcha)")

# # Til tanlash
# language = st.selectbox("Tilni tanlang:", ("Inglizcha", "Ruscha", "O'zbekcha"))

# # Til kodi moslamasi
# lang_code = {"Inglizcha": "en-US", "Ruscha": "ru-RU", "O'zbekcha": "uz-UZ"}

# # Tugma bosilganda
# if st.button("Ovoz yozib olish va matnga aylantirish"):
#     st.write(f"Ovoz yozib olinmoqda ({language})...")
#     recognizer = sr.Recognizer()

#     try:
#         with sr.Microphone() as source:
#             # Foydalanuvchi ovozini yozib olish
#             recognizer.adjust_for_ambient_noise(source)
#             st.info("Mikrofondan gapiring...")
#             audio = recognizer.listen(source, timeout=10)

#             # Matnga aylantirish
#             st.write("Matnga aylantirilmoqda...")
#             transcription = recognizer.recognize_google(audio, language=lang_code[language])
#             st.success("Matn muvaffaqiyatli tanildi!")
#             st.text_area("Taniqli matn:", transcription)
#     except sr.UnknownValueError:
#         st.error("Ovozni tushunib bo'lmadi. Iltimos, qaytadan urinib ko'ring.")
#     except sr.RequestError as e:
#         st.error(f"Google Speech Recognition xizmati bilan bog'lanib bo'lmadi; {e}")
