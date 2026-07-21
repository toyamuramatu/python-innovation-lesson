import streamlit as st
st.title("🐾腹ペコペット育成")

if 'hunger' not in st.session_state:
    st.session_state.hunger=50

if st.session_state.hunger>=80:
    st.write("😄")
elif st.session_state.hunger>=30:
    st.write("😐")
else:
    st.write("😭")

st.write(st.session_state.hunger)

if st.button("🍖エサをあげる"):
    if st.session_state.hunger>=0 and st.session_state.hunger<=90:
        st.session_state.hunger+=10

if st.button("🥏遊ぶ"):
    if st.session_state.hunger>=15 and st.session_state.hunger<=100:
        st.session_state.hunger-=15