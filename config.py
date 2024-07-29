from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TRANSCRIPT_LANGUAGES = os.getenv("TRANSCRIPT_LANGUAGES", "ja,en").split(",")

genai.configure(api_key=GEMINI_API_KEY)
