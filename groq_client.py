from dotenv import load_dotenv
from groq import Groq
from schemas import weather_tool,currency_tool
import os


load_dotenv()

client = Groq(api_key=os.getenv("groq_api_key"))
def get_conversarion(message : list):
    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages = message,
        tools= [weather_tool,currency_tool],
        tool_choice="auto"
    )
    return response

def get_streaming(messages):
    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages=messages,
        stream=True
    )
    return response