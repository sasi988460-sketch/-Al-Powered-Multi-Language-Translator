import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY") or "AIzaSyDv91nV6mhoGBood7ujIu2wFRKiBHGKsaA"
try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")
except Exception as e:
    st.error(f"Failed to configure Gemini: {e}")
def translate_text(text, source_language, target_language):
    """Translates text using the pre-initialized model instance."""
    prompt = (
        f"Translate the following text from {source_language} to {target_language}. "
        f"Only provide the translated text, no extra conversation: {text}"
    )
    response = model.generate_content(prompt)
    return response.text
st.set_page_config(page_title="AI-Powered Translator", page_icon="🌐")
st.header("🌐 AI-Powered Translator")
text = st.text_area("📝 Enter text to translate:", height=150)
col1, col2 = st.columns(2)
with col1:
    source_language = st.selectbox("🌍 From:", ["English", "Spanish", "French", "German", "Chinese", "Japanese"])
with col2:
    target_language = st.selectbox("🌍 To:", ["Spanish", "English", "French", "German", "Chinese", "Japanese"])
if st.button("🔄 Translate", use_container_width=True):
    if text.strip():
        with st.spinner("Processing translation..."):
            try:
                translated_text = translate_text(text, source_language, target_language)
                st.subheader("🟣 Translated Text:")
                st.success(translated_text)
            except Exception as e:
                st.error(f"⚠️ Error: {str(e)}")
    else:
        st.warning("⚠️ Please enter some text to translate.")
