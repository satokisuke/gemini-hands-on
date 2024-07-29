from typing import List

from youtube_transcript_api import YouTubeTranscriptApi


def transcribe(video_id: str, languages: List[str]) -> str:
    """
    YouTube文字起こしAPIを実行します。
    :param video_id:
    :param languages:
    :return:
    """
    response = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
    return ' '.join(map(lambda item: item['text'], response))
