import streamlit as st
st.title("☆カウンターアプリ")

if 'stars' not in st.session_state:
    st.session_state.stars=0

if st.button("☆を増やす"):
    st.session_state.stars+=1

if st.button("☆をリセット"):
    st.session_state.stars=0

for i in range(st.session_state.stars):
    st.write("☆")