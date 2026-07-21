import streamlit as st

text_contents = """これはダウンロードできるテキストファイルだよ。
複数行にわたるテキストでも大丈夫!
Streamlitでファイルダウンロード機能を使ってみよう!"""

st.download_button(
    label="テキストファイルをダウンロード",
    data=text_contents,
    file_name="sample_text.txt",
    mime="text/plain"
)

