from enum import StrEnum
from typing import List

from pydantic import BaseModel

import streamlit as st


class Author(StrEnum):
    User = "user"
    Assistant = "assistant"


class Message(BaseModel):
    author: Author
    message: str
    code: str
    video_id: str


def get_history() -> List[Message]:
    """
    セッションから履歴を取得します。
    :return:
    """
    if 'history' not in st.session_state:
        st.session_state['history'] = []
    return list(map(lambda item: Message(**item), st.session_state['history']))


def add_message(message: str, author: Author = Author.User, code: str = "", video_id: str = ""):
    """
    セッションにメッセージを保存します。
    :param message:
    :param author:
    :param code:
    :param video_id:
    """
    message = Message(author=author, message=message, code=code, video_id=video_id)
    st.session_state['history'].append(message.model_dump())


def show_message(message: Message):
    """
    メッセージを適切なフォーマットにして表示します。
    ユーザー、アシスタントといった投稿者の種別によって表示を出し分けます。
    :param message:
    :return:
    """
    video_id = message.video_id
    text = message.message
    code = message.code
    if message.author == Author.User:
        with st.chat_message("user"):
            st.write(text)
            if len(video_id) > 0:
                st.video(f"https://www.youtube.com/watch?v={video_id}")
        return

    with st.chat_message("assistant"):
        st.write(text)
        if len(code) > 0:
            st.code(code)
