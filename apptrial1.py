import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import os
import time
import glob
from gtts import gTTS
from googletrans import Translator

try:
    os.mkdir("temp")
except:
    pass

def text_to_speech(input_language, output_language, text):
    translation = translator.translate(text, src=input_language, dest=output_language)
    trans_text = translation.text
    tts = gTTS(trans_text, lang=output_language, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, trans_text
def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)

def runvoice(text):
    result, output_text = text_to_speech(input_language, output_language, text)
    audio_file = open(f"temp/{result}.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3",start_time=0)
    st.write(f" {output_text}")

translator = Translator()

in_lang = st.selectbox(
    "Select your output language",
    ("English", "Tamil", "Telugu", "Kannada", "Malayalam", "Kannada"),)
text = "Welcome To Water Quality Analysis Software"
if in_lang == "English":
    output_language = "en"
elif in_lang == "Tamil":
    output_language = "ta"
elif in_lang == "Telugu":
    output_language = "te"
elif in_lang == "Hindi":
    output_language = "hi"
elif in_lang == "Malayalam":
    output_language = "ml"
elif in_lang == "Kannada":
    output_language = "kn"

input_language="en"


# Web App Title
st.title('''
## The Water Quality Analysis App''')
runvoice("The Water Quality Analysis App")

st.markdown('''### This is the **Study App** created in Streamlit using the **pandas-profiling** library.
****Credit:**** App built in `Python` + `Streamlit` by [JASHVANTH S R ](https://www.linkedin.com/in/jashvanth-s-r-476646213)[HARUL GANESH S B ](https://www.linkedin.com/in/harul-ganesh/)[BALAJI S ](https://www.linkedin.com/in/balaji-s-csbs-dept-03790a202/)[GOWTHAM H](https://www.linkedin.com/in/gowtham-haribabu-9425861bb/)
---
''')
runvoice("This is the Software used to study the Characteristics of Water. This software is created in Streamlit using the panda's profiling library.\
    Courtesy :  Software built in 'Python' and 'Streamlit' by JASHVANTH S R,BALAJI S,HARUL GANESH S B,GOWTHAM H")






# Upload CSV data
with st.sidebar.header('1. Upload your CSV data'):
    runvoice("Upload your CSV data")
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)
""")
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    runvoice(text="Input DataFrame")
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    runvoice(text="Pandas Profiling Report")

    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    runvoice("Awaiting for CSV file to be uploaded")
    if st.button('Press to use Example Dataset'):
        runvoice(text="Press to use Example Dataset")
        @st.cache
        def load_data():
            a = pd.DataFrame(
            np.random.rand(100, 5),
            columns=['a', 'b', 'c', 'd', 'e'])
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        runvoice(text="Input DataFrame")
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        runvoice(text="Panda's Profiling Report")
        st_profile_report(pr)
remove_files(7)
