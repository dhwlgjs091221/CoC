import streamlit as st
import asyncio
from chat_client import ChatClient  # chat_client.py에서 ChatClient 정의했다고 가정

# 1. Streamlit 페이지 설정은 반드시 최상단에
st.set_page_config(page_title="탐사자 생성 + 채팅", layout="wide")

# 2. 이벤트 루프 초기화 (최초 실행 시에만)
if "loop" not in st.session_state:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    st.session_state.loop = loop
else:
    loop = st.session_state.loop

# 3. 채팅 클라이언트 초기화 및 연결
if "chat_client" not in st.session_state:
    st.session_state.chat_client = ChatClient()
    # connect()는 비동기 함수이므로 이벤트 루프에 task로 등록
    st.session_state.task = loop.create_task(st.session_state.chat_client.connect())

# UI 구성
st.title("크툴루 탐사자 생성 + 멀티채팅")

# --- 탐사자 생성 UI 예시 ---
name = st.text_input("탐사자 이름")
if st.button("탐사자 저장"):
    # 저장 로직 예시 (구현 필요)
    st.success(f"{name} 탐사자가 저장되었습니다.")

st.markdown("---")

# --- 채팅 UI ---
username = st.text_input("닉네임", key="username")
message = st.text_input("메시지 입력", key="message")
send_button = st.button("전송")

if send_button and message.strip() != "":
    from asyncio import run_coroutine_threadsafe
    msg = f"{username}: {message}"
    # run()도 비동기 함수이니 run_coroutine_threadsafe로 실행
    run_coroutine_threadsafe(
        st.session_state.chat_client.run(msg),
        loop
    )
    st.session_state.message = ""  # 메시지 입력 초기화

# 채팅 메시지 보여주기 (간단 예시)
st.subheader("채팅 내용")
for chat_msg in st.session_state.chat_client.messages:
    st.write(chat_msg)
