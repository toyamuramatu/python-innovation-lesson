import streamlit as st
import random
st.title("確率ほんまかいなイカサマ防止マプリ")

def kakuritsu(wariai):
    hiku=random.choice([1,2,3,4,5,6,7,8,9,10])


kakuritsu(10)

if 'nankaiyattaka' not in st.session_state:
    st.session_state.nannkaiyattaka=0
