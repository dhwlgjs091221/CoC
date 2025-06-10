
import streamlit as st
from character_manager import create_character, save_character, load_character
import os

st.set_page_config(page_title="크툴루의 부름 탐사자 생성기", layout="wide")
#st.set_page_config(page_title="탐사자 생성 + 채팅", layout="wide")
st.title("🔍 크툴루의 부름 탐사자 생성기")

menu = st.sidebar.radio("메뉴 선택", ["탐사자 생성", "탐사자 불러오기"])

if menu == "탐사자 생성":
    st.header("🧍 탐사자 정보 입력")

    name = st.text_input("이름")
    occupation = st.text_input("직업")
    age = st.number_input("나이", 15, 90, 25)

    st.subheader("능력치 입력")
    strength = st.slider("근력(STR)", 1, 100, 50)
    dexterity = st.slider("민첩(DEX)", 1, 100, 50)
    intelligence = st.slider("지능(INT)", 1, 100, 50)
    power = st.slider("정신력(POW)", 1, 100, 50)
    appearance = st.slider("매력(APP)", 1, 100, 50)
    education = st.slider("교육(EDU)", 1, 100, 50)

    if st.button("💾 저장하기"):
        character = create_character(name, occupation, age, strength, dexterity,
                                     intelligence, power, appearance, education)
        save_character(character)
        st.success(f"{name} 탐사자가 저장되었습니다.")

elif menu == "탐사자 불러오기":
    st.header("📂 탐사자 불러오기")
    files = [f for f in os.listdir("sample_data") if f.endswith(".json")]

    selected_file = st.selectbox("불러올 탐사자 선택", files)

    if st.button("📤 불러오기"):
        character = load_character(os.path.join("sample_data", selected_file))
        st.json(character)


st.title("🧍 탐사자 생성 + 💬 멀티 채팅")

# 채팅 클라이언트 초기화
if "chat_client" not in st.session_state:
    st.session_state.chat_client = ChatClient()

# 채팅 메시지 보내기
with st.form("chat_form"):
    username = st.text_input("이름", key="chat_user")
    message = st.text_input("메시지", key="chat_message")
    submitted = st.form_submit_button("전송")

    if submitted and message.strip():
        asyncio.run(st.session_state.chat_client.run(f"{username}: {message}"))

# 받은 메시지 표시
st.subheader("🔊 실시간 채팅 로그")
for msg in st.session_state.chat_client.messages[-20:]:
    st.markdown(f"- {msg}")
