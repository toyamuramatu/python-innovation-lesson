import streamlit as st

a=0
st.title("実習:簡単な挨拶アプリ")
name=st.text_input("名前を入力してね")
if name:
    a=1
if st.button("挨拶する"):
    if a==1:
        st.write("今日も素晴らしい一日ですね。")
    else:
        st.write("名前を入力してください")