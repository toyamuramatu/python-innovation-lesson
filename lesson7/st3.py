import streamlit as st
st.title("カフェのポイントカード")

if 'points' not in st.session_state:
    st.session_state.points=0

if 'rank' not in st.session_state:
    st.session_state.rank="ノーマル"

def add_points(amount):
    st.session_state.points+=amount
    if st.session_state.points>=20:
        st.session_state.rank="ゴールド"
    elif st.session_state.point>=10:
        st.session_state.rank="シルバー"
    else:
        st.session_state.rank="ノーマル"

st.write(f"現在のポイントは{st.session_state.points}ポイントで、{st.session_state.rank}会員です。")

if st.button("コーヒーを買う"):
    add_points(2)
if st.button("ケーキを買う"):
    add_points(5)
if st.button("リセット"):
    st.session_state.points=0
    st.session_state.rank="ノーマル"