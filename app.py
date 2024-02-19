import streamlit as st
from utils import get_answer_csv

import streamlit as st

st.header('Chat with CSV :clipboard:')
uploaded_file = st.file_uploader('Upload a CSV fiile here', type=['csv'])

if uploaded_file is not None:
    query = st.text_area('Ask any Question related to the Document')
    button = st.button('Submit')

    if button:
        st.write(get_answer_csv(uploaded_file, query))