import streamlit as st

import random
# 動物の鳴き声を返す関数
def get_sound(animal):
    if animal == "dog":
        return "ワンワン！"
    if animal == "cat":
        return "ニャーニャー！"
    else:
        return "その動物はデータがありません！"
st.title("動物の鳴き声アプリ")
selected = st.selectbox("動物を選んでね", ["dog", "cat", "bird"])
if st.button("鳴き声を聞く"):
    st.write(f"{get_sound(selected)}")


animal = st.text_input("好きな動物は？")
if animal:
    st.write(f"動物: {animal}")

col1, col2 = st.columns(2)
with col1:
    st.write("こっちが左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左右左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左左")
with col2:
    st.write("こっちが右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右右左右右右右右右右右右右右右右右右右右右右")

import streamlit as st
tab1, tab2 = st.tabs(["情報", "設定"])
with tab1:
    st.write("アプリ情報")
with tab2:
    st.slider("設定値", 0, 100)



st.title("今日の運勢占い")
if st.button("おみくじを引く！"):
    fortune = random.choice(["大吉", "中吉", "小吉", "凶"]) #リストから一つランダムに選ぶ関数
st.header(f"運勢: **{fortune}**")
if fortune == "大吉":
    st.balloons(); st.success("良い日！")
elif fortune == "中吉":
    st.info("いいことあるかも！")
elif fortune == "小吉":
    st.warning("少し注意。")
else:
    st.error("今日は慎重に。")