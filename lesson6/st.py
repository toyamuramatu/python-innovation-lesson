import streamlit as st

import random


st.title("今日の運勢占い")
def omikuzi():
    if st.button("おみくじを引く！"):
        fortune = random.choice([1,2,3,4,5,6,7,8,9,10])
        st.write(fortune)
        if fortune <=2:
            st.header("大吉")
            st.balloons()
            st.success("良い日！")
        elif fortune <=6:
            st.header("中吉")
            st.info("いいことあるかも！")
        elif fortune <=9:
            st.header("小吉")
            st.warning("少し注意。")
        else:
            st.header("凶")
            st.error("今日は慎重に。")

omikuzi()