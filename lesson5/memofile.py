import streamlit as st

st.title("シンプルメモ帳")

memo_text = st.text_area("メモを入力してね",height=200)

file_name = st.text_input("保存するファイル名","memo.txt")

if memo_text:
    st.download_button(
        label="メモをダウンロード",
        data=memo_text,
        file_name=file_name,
        mime="text/plain"
    )
else:
    st.info("メモを入力するとダウンロードボタンが表示されるよ")


st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", 
caption="Streamlitロゴ ")

st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", 
caption="幅を 300pxに 指定", width=300)