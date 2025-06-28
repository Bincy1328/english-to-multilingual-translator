import streamlit as st
from googletrans import Translator
from gtts import gTTS
from mutagen.mp3 import MP3
import os
import uuid

# --- Setup ---
st.set_page_config(page_title="🌐 Language Translator", layout="centered")
st.title("🌍 English to Any Language Translator")
st.markdown("Translate your vibes from English to Tamil or any language ✨")

# --- Input Text ---
input_text = st.text_area("✏ Type something (any language)", placeholder="e.g., Hello! How are you?")

# --- Language Options ---
languages = {
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "Japanese": "ja",
    "German": "de",
    "Arabic": "ar",
    "Russian": "ru",
    "Malayalam":"ml"
}
target_lang = st.selectbox("🌐 Translate to", list(languages.keys()))
target_lang_code = languages[target_lang]

# --- Translate & TTS ---
if st.button("🚀 Translate"):
    if not input_text.strip():
        st.warning("Please type something first.")
    else:
        try:
            # Translate with auto-detection
            translator = Translator()
            translated = translator.translate(input_text, dest=target_lang_code)
            translated_text = translated.text
            detected_lang = translated.src

            st.subheader(f"✅ Translated to {target_lang}:")
            st.success(translated_text)
            st.caption(f"🕵 Detected input language: {detected_lang}")

            # Generate speech using gTTS
            tts = gTTS(translated_text, lang=target_lang_code)
            audio_file = f"audio_{uuid.uuid4().hex}.mp3"
            tts.save(audio_file)

            # Use mutagen to get audio duration
            audio_info = MP3(audio_file)
            duration = int(audio_info.info.length)
            mins, secs = divmod(duration, 60)

            # Play audio
            st.audio(audio_file, format="audio/mp3")
            st.caption(f"⏱ Duration: {mins} min {secs} sec")

            # Download button
            with open(audio_file, "rb") as f:
                st.download_button("⬇ Download Translated Audio", f, file_name="translated_audio.mp3", mime="audio/mp3")
                # Optional: remove the file to keep system clean
            os.remove(audio_file)

        except Exception as e:
            st.error(f"Error:{e}")

