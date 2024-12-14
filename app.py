import streamlit as st
import speech_recognition as sr

# Streamlit sarlavha
st.title("Multilingual Speech-to-Text (STT) Web App")
st.write("Ovozli matnni yozib olish va matnga aylantiruvchi veb-dastur (Inglizcha, Ruscha, O'zbekcha)")

# Til tanlash
language = st.selectbox("Tilni tanlang:", ("Inglizcha", "Ruscha", "O'zbekcha"))

# Til kodi moslamasi
lang_code = {"Inglizcha": "en-US", "Ruscha": "ru-RU", "O'zbekcha": "uz-UZ"}

# Tugma bosilganda
if st.button("Ovoz yozib olish va matnga aylantirish"):
    st.write(f"Ovoz yozib olinmoqda ({language})...")
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            # Foydalanuvchi ovozini yozib olish
            recognizer.adjust_for_ambient_noise(source)
            st.info("Mikrofondan gapiring...")
            audio = recognizer.listen(source, timeout=10)

            # Matnga aylantirish
            st.write("Matnga aylantirilmoqda...")
            transcription = recognizer.recognize_google(audio, language=lang_code[language])
            st.success("Matn muvaffaqiyatli tanildi!")
            st.text_area("Taniqli matn:", transcription)
    except sr.UnknownValueError:
        st.error("Ovozni tushunib bo'lmadi. Iltimos, qaytadan urinib ko'ring.")
    except sr.RequestError as e:
        st.error(f"Google Speech Recognition xizmati bilan bog'lanib bo'lmadi; {e}")
