import streamlit as st
MENU = {
    "バーガー": {"チーズバーガー": 250, "てりやきバーガー": 400, "ワッパー": 600},
    "サイド": {"フライドポテト": 150, "チキンナゲット": 200, "オニオンリング": 250},
    "ドリンク": {"コーラ": 100, "メロンソーダ": 150, "アイスコーヒー": 150}
}
if "total_price" not in st.session_state:
    st.session_state.update(total_price=0, message="お好みのセットを作ってください！")

def order_set(burger, side, drink):
    st.session_state.total_price += MENU["バーガー"][burger] + MENU["サイド"][side] + MENU["ドリンク"][drink] - 100
    st.session_state.message = f"【注文追加】{burger}セット（-100円引）をカートに入れました！"

st.title("🍔 バーガーショップ・カスタムセット注文")
st.info(st.session_state.message)
st.subheader(f"現在の合計金額: {st.session_state.total_price} 円")
b = st.selectbox("バーガーを選択", MENU["バーガー"].keys())
s = st.selectbox("サイドを選択", MENU["サイド"].keys())
d = st.selectbox("ドリンクを選択", MENU["ドリンク"].keys())
if st.button("🛒 この組み合わせでセット注文（100円引）"):
     order_set(b, s, d); st.rerun()
if st.button("🔄 お会計（リセット）"):
    st.session_state.update(total_price=0, message="お好みのセットを作ってください！"); st.rerun()



