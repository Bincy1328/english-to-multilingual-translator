import streamlit as st
from googletrans import Translator

# Set page config
st.set_page_config(page_title="🌐 Language Translator", layout="centered")

st.title("🌍 English to Any Language Translator")
st.markdown("Translate your vibes from English to Tamil or any language ✨")

# Input text
input_text = st.text_area("✏ Type something in English")

# Language options
languages = {
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "Japanese": "ja",
    "German": "de",
    "Arabic": "ar",
    "Russian": "ru"
}

target_lang = st.selectbox("🌐 Select a language to translate into", list(languages.keys()))

if st.button("🚀 Translate"):
    if input_text.strip() == "":
        st.warning("Type something first, macha 😅")
    else:
        translator = Translator()
        result = translator.translate(input_text, dest=languages[target_lang])
        st.subheader(f"🈶 Translated ({target_lang}):")
        st.success(result.text)
