from chatflow import ChatFlow, Session, Message
import pytest
from datetime import datetime

def test_add_session():
    chatflow = ChatFlow()
    chatflow.add_session(1, Message(text="Hello", timestamp=datetime.now()))
    assert len(chatflow.get_sessions()) == 1

def test_get_sessions():
    chatflow = ChatFlow()
    chatflow.add_session(1, Message(text="Hello", timestamp=datetime.now()))
    chatflow.add_session(2, Message(text="Hi", timestamp=datetime.now()))
    sessions = chatflow.get_sessions()
    assert len(sessions) == 2
    assert sessions[0].id == 1
    assert sessions[1].id == 2

def test_get_session_messages():
    chatflow = ChatFlow()
    chatflow.add_session(1, Message(text="Hello", timestamp=datetime.now()))
    chatflow.add_session(1, Message(text="How are you?", timestamp=datetime.now()))
    messages = chatflow.get_session_messages(1)
    assert len(messages) == 2
    assert messages[0].text == "Hello"
    assert messages[1].text == "How are you?"

def test_send_message():
    chatflow = ChatFlow()
    chatflow.send_message(1, "Hello")
    messages = chatflow.get_session_messages(1)
    assert len(messages) == 1
    assert messages[0].text == "Hello"

def test_edge_case_empty_sessions():
    chatflow = ChatFlow()
    assert len(chatflow.get_sessions()) == 0

def test_edge_case_non_existent_session():
    chatflow = ChatFlow()
    messages = chatflow.get_session_messages(1)
    assert len(messages) == 0
