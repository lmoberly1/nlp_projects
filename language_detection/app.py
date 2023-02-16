import pickle
import string
import streamlit as st
import webbrowser

global Lrdetect_Model

Lrdetect_File = open('model.pckl', 'rb')
Lrdetect_Model = pickle.load(Lrdetect_File)
Lrdetect_File.close()
st.title('Language Detection Tool')
input_test = st.text_input('Enter text to detect language')

button_clicked = st.button('Get Predicted Language')
if button_clicked:
    st.text(Lrdetect_Model.predict([input_test]))