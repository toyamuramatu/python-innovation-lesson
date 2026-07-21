import streamlit as st

st.title("マイプロフィール")

name=st.text_input("名前を入力してね:")

ziko=st.text_area("自己紹介を書いてね:")

tan=st.date_input("誕生日を選んでね")

botan= st.button("あなたの情報")
if botan:
    st.write(name)
    st.write(ziko)
    st.write(tan)
