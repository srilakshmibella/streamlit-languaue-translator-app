from translate import Translator
import googletrans
import streamlit as st


st.title("Language Translator")
text=st.text_input("Enter a text")
choices=googletrans.LANGUAGES
choices=list(choices.values())
st.selectbox("Choose a Language",(choices))
text1=st.text_input('Re-enter Chosen Language')
translator=Translator(to_lang=text1)
translation=translator.translate(text)
st.write(translation)
st.button('Translate',translation)
