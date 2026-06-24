from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict

@dataclass
class Message:
    text: str
    timestamp: datetime

@dataclass
class Session:
    id: int
    messages: List[Message]

class ChatFlow:
    def __init__(self):
        self.sessions: Dict[int, Session] = {}

    def add_session(self, session_id: int, message: Message):
        if session_id not in self.sessions:
            self.sessions[session_id] = Session(id=session_id, messages=[])
        self.sessions[session_id].messages.append(message)

    def get_sessions(self):
        return list(self.sessions.values())

    def get_session_messages(self, session_id: int):
        return self.sessions.get(session_id, Session(id=session_id, messages=[])).messages

    def send_message(self, session_id: int, message: str):
        self.add_session(session_id, Message(text=message, timestamp=datetime.now()))
