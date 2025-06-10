import streamlit as st
import asyncio
from chat_client import ChatClient

# 페이지 설정 (최상단에)
st.set_page_config(page_title="크툴루 탐사자 생성 + 멀티채팅", layout="wide")

# 이벤트 루프 초기화
if "loop" not in st.session_state:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    st.session_state.loop = loop
else:
    loop = st.session_state.loop

# 채팅 클라이언트 초기화 및 연결
if "chat_client" not in st.session_state:
    st.session_state.chat_client = ChatClient()
    st.session_state.task = loop.create_task(st.session_state.chat_client.connect())

st.title("크툴루 탐사자 생성 + 멀티채팅")

# 탐사자 생성 UI (간단 예시)
name = st.text_input("탐사자 이름")
if st.button("탐사자 저장"):
    st.success(f"{name} 탐사자가 저장되었습니다.")

st.markdown("---")

# 채팅 UI
username = st.text_input("닉네임", key="username")
message = st.text_input("메시지 입력", key="message", value="")  # 여기에 value="" 넣음
send_button = st.button("전송")

if send_button and message.strip() != "":
    from asyncio import run_coroutine_threadsafe
    msg = f"{username}: {message}"
    run_coroutine_threadsafe(
        st.session_state.chat_client.run(msg),
        loop
    )
    # 메시지 초기화 코드는 삭제함

# 채팅 메시지 보여주기
st.subheader("채팅 내용")
for chat_msg in st.session_state.chat_client.messages:
    st.write(chat_msg)
