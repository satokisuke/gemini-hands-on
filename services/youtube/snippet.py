import requests
from pydantic import BaseModel
import urllib.parse

YOUTUBE_API_URL = "https://content-youtube.googleapis.com/youtube/v3/videos"


class YoutubeSnippet(BaseModel):
    video_id: str
    title: str
    description: str


def fetch_snippet(video_id: str, api_key: str) -> YoutubeSnippet:
    """
    YouTube Data API v3よりの動画概要を取得します。
    :param video_id:
    :param api_key:
    :return:
    """
    if api_key is None or len(api_key) == 0:
        raise ValueError("YouTube API key is empty")

    # サニタイズ
    video_id = urllib.parse.quote(video_id)
    api_key = urllib.parse.quote(api_key)

    response = requests.get(f"{YOUTUBE_API_URL}?id={video_id}&key={api_key}&part=snippet")
    response.raise_for_status()

    result = response.json()
    items = result.get('items', [])
    if len(items) == 0:
        raise ValueError("No item found")
    item = items[0]
    snippet = item.get("snippet")
    if not snippet:
        raise ValueError("No snippet found")
    return YoutubeSnippet(
        video_id=video_id,
        title=snippet.get("title", ""),
        description=snippet.get("description", ""),
    )
