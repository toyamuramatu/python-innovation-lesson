import streamlit as st
level = st.slider("キャラクターのレベルを選択", 0, 100, 50)
st.write(f"選択されたレベル: {level}レベル")



show_details=st.checkbox("特殊能力を持っている")

if show_details:
    st.write("特殊能力を持っています")
else:
    st.write("特殊能力を持っていません")



nito=st.radio("キャラクターの職業を選択",["戦士","魔法使い","盗賊"])
st.write(f"あなたの選んだ職業:{nito}")



umare=st.selectbox(
    "出身地を選んでね",
    ["砂漠","森","雪国","都市"]
)
st.write(f"あなたが選んだ出身地:{umare}")



options=st.multiselect(
    "好きな武器を選択(複数選択可)",
    ["剣","弓","杖","ナイフ"]
)
if options:
    st.write(f"あなたが選んだ武器:{','.join(options)}")

show_profile = st.button("キャラクタープロフィールを表示")

# ボタンが押されたらプロフィール表示
if show_profile:
    st.markdown("---")
    st.header("🧙‍♂️ あなたのキャラクタープロフィール")

    st.subheader("📋 基本情報")
    cols = st.columns(3)
    cols[0].metric(label="🛡️ クラス", value=nito)
    cols[1].metric(label="🗺️ 出身地", value=umare)
    cols[2].metric(label="🎚️ レベル", value=level)

    st.markdown("---")

    st.subheader("✨ 特徴・能力")
    if show_details:
        st.success("✅ 特殊能力あり！")
    else:
        st.error("❌ 特殊能力なし")

    st.markdown("---")

    st.subheader("⚔️ 得意な武器")
    if options:
        st.info("選んだ武器：")
        for weapon in options:
            st.write(f"・{weapon}")
    else:
        st.warning("武器は選ばれていません。")

    st.markdown("---")