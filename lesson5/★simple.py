import streamlit as st

try:
    st.title("メモ帳📒")
    text = st.text_area("",height=300)

    if text:
        count=len(text)
        st.write(f"{count}文字📑")

    filename = st.text_input("保存するファイル名📝")

    if text:
        st.download_button(
            label="メモをダウンロード⬇️",
            data=text,
            file_name=filename,
            mime="text/plain"
        )

except:
    print("'E R R O R'")