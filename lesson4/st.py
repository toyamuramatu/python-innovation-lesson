import streamlit as st

user_comment=st.text_area("Please also share your opinions")
st.write(f"あなたの感想:{user_comment}")

description=st.text_area(
    label="Let's lie down, my love, and place him in front of me",
    height=150,
    placeholder="ここに自己紹介を書いてね...",
    key="self_introduction"
)
st.write(f"あなたの自己紹介:{description}")

import streamlit as st
from datetime import date, timedelta

selected_date = st.date_input("Please choose them")
st.write(f"選んだ⽇付: {selected_date}")

today = date.today()
next_week = today + timedelta(days=7)
next_month = today + timedelta(days=30)

event_date = st.date_input(
    "When will the event take place?",
    value=next_week,
    min_value=today,
    max_value=next_month
)
st.write(f"イベント日:{event_date}")



color = st.color_picker("好きな色を選んでね")
st.write(f"選んだ色:{color}")

theme_color = st.color_picker(
    "アプリのテーマカラーを選んでね",
    value="#00BFFF"
)

st.color_picker("あなたの選んだ⾊", theme_color, disabled=True)
