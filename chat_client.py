import asyncio

class ChatClient:
    def __init__(self):
        self.messages = []
        self._connected = False

    async def connect(self):
        # 서버 연결 시뮬레이션 (실제론 웹소켓 등 연결 코드)
        await asyncio.sleep(0.1)
        self._connected = True
        self.messages.append("채팅 서버에 연결되었습니다.")

    async def run(self, msg):
        if not self._connected:
            self.messages.append("서버에 연결되지 않았습니다.")
            return
        # 메시지 전송 시뮬레이션 (실제로 서버에 보내는 코드 필요)
        await asyncio.sleep(0.1)  # 네트워크 대기 흉내
        self.messages.append(msg)
