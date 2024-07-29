import re


def extract_video_id(text: str) -> str:
    """
    ユーザーの入力からYouTube動画IDを取得します。
    :param text:
    :return:
    """
    url_pattern = r"https?:\/\/(?:www\.)?youtube\.com\/watch\?([\w+]=.*&)*v=([\w-]+)"
    matches = re.search(url_pattern, text, re.M)
    if matches:
        result = re.sub(r"^.+v=", "", matches[0])
        result = re.sub(r"[^\w-]", "", result)
        return result
    return ""
