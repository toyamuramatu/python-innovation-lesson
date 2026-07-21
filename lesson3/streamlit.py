import streamlit as st
age = st.slider("年齢を 選択", 0, 100, 25)
st.write(f"選択された年齢: {age}歳")

price_range = st.slider("価格帯を 選択",0, 10000, (2000, 5000)  # (min, max, (default_min, default_max))
)

st.write(f"選択された価格帯: {price_range[0]}円から{price_range[1]}円")
step_value = st.slider("5刻みで選択",0, 100, 25, step=5)

st.write(f"選択された値: {step_value}")

show_details=st.checkbox("詳細を確認する")

if show_details:
    st.write("ここに詳細情報を表示します")
    st.write("さらに多くの情報...")
else:
    st.write("チェックボックスをオンにすると詳細が表示されるよ")

st.write("###好きな果物を選んでね")
apple=st.checkbox("リンゴ")
banana=st.checkbox("バナナ")
orange=st.checkbox("オレンジ")

selected_fruits=[]
if apple:
    selected_fruits.append("リンゴ")
if banana:
    selected_fruits.append("バナナ")
if orange:
    selected_fruits.append("オレンジ")

if selected_fruits:
    st.write(f"選んだ果物: {', '.join(selected_fruits)}")
else:
    st.write("まだ何も選んでないよ")

option=st.radio("好きな色を選んでね",["赤","青","緑","黄色"])

st.write(f"あなたの選んだ色:{option}")

option=st.selectbox(
    "好きな果物を選んでね",
    ["リンゴ","バナナ","オレンジ","ぶどう","メロン"]
)
st.write(f"あなたが選んだ果物:{option}")

fruits_dict={
    "リンゴ":"🍎",
    "バナナ":"🍌",
    "オレンジ":"🍊",
    "ブドウ":"🍇"
}
fruit=st.selectbox("フルーツを選択",list(fruits_dict.keys()))
st.write(f"選んだフルーツの絵文字:{fruits_dict[fruit]}")

options=st.multiselect(
    "好きな色を選んでね(複数選択可)",
    ["赤","青","緑","黄色","紫","オレンジ"]
)

if options:
    st.write(f"あなたが選んだ色:{','.join(options)}")
else:
    st.write("色を選んでね")