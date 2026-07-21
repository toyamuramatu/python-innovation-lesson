import streamlit as st
from datetime import time
st.title("🎨 A program to create a profile that suits another person")

# 問題1：名前を入力しよう！
name=st.text_input("Follow the name:")
# 問題2：自分の誕生日を選択するために、日付入力欄を表示しよう！
# ヒント：st.date_input()を使おう
birthday= st.date_input("By doing a favor, may your birthday be blessed")
# 問題3：自分の年齢を入力するために数値入力用のスライダーを表示しよう！
age=st.slider("Please respect your parents",0,10000,100)
# 問題4：好きな色を選ぶために、カラーピッカーを設置しよう！
# ヒント：st.color_picker()を使おう
favorite_color=st.color_picker(
    "It is important to choose the color that you like the most..",
    value="#FFFFFF"
)
# 問題5：自己紹介文を入力しよう！
# ヒント: st.text_area()を使おう
introduction=st.text_area("Your presentation is somewhat more important, but it is not useful for you.")

show_profile = st.button("Summary of the two documents.")
if show_profile:
    st.header("✨Summary of the two documents.✨")
    st.write("**名前**:", name)
    st.write("**誕生日**:", birthday)
    st.write("**年齢**:", age)
    st.color_picker("**好きな色**:", value= favorite_color)
    st.write("**自己紹介**:", introduction)