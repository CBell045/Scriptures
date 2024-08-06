import numpy as np
import streamlit as st
import pandas as pd
from streamlit_extras.stoggle import stoggle

scriptures = pd.read_parquet("./data/scriptures.parquet")

heart_scriptures = scriptures['scripture_text'].str.contains("heart", case=False)

if 'show_scripture' not in st.session_state:
    st.session_state.show_scripture = False

if 'show_reference' not in st.session_state:
    st.session_state.show_reference = False

if 'scripture' not in st.session_state:
    st.session_state.scripture = None

def show_scripture():
    st.session_state.show_scripture = True
    st.session_state.show_reference = False

def show_reference():
    st.session_state.show_reference = True

def generate_scripture(_volume, _heart_mode):
    if _heart_mode:
        _scriptures = scriptures[heart_scriptures]
    if volume is None or volume == "Any":
        return _scriptures.sample()
    else:
        return _scriptures[_scriptures.volume_title == _volume].sample()



st.sidebar.title("Options")
st.sidebar.subheader("Select a volume of scripture")
options = np.append("Any", scriptures.volume_title.unique())
volume = st.sidebar.selectbox("Volume", options, index=3)



st.title("Random Scripture Generator")
st.subheader("Click the button below to generate a random scripture")


heart_mode = st.toggle("Heart Mode", True)

if st.button("Generate", on_click=show_scripture): 
    scripture = generate_scripture(volume, heart_mode)
    st.session_state.scripture = scripture
    st.write(scripture['scripture_text'].values[0])
    stoggle(
    "Show Reference",
    f"{scripture['verse_title'].values[0]}"
    )
