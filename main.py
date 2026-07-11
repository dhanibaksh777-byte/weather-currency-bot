from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from groq_client import get_conversarion, get_streaming
from pydantic import BaseModel
from tools import get_currency, get_weather
import json


class ChatRequest(BaseModel):
    message: str


app = FastAPI()


def stream_generator(messages):
    response = get_streaming(messages)
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content:
            yield content


@app.post("/chat")
def chat(request: ChatRequest):
    messages = [{"role": "user", "content": request.message}]
    response = get_conversarion(messages)
    message = response.choices[0].message

    if message.tool_calls:
        tool_call = message.tool_calls[0]
        function_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        if function_name == "get_weather":
            result = get_weather(**arguments)
        elif function_name == "get_currency":
            result = get_currency(**arguments)
        else:
            return {"error": "unknown function"}

        messages.append({
            "role": "assistant",
            "content": message.content,
            "tool_calls": [
                {
                    "id": tool_call.id,
                    "type": "function",
                    "function": {
                        "name": tool_call.function.name,
                        "arguments": tool_call.function.arguments
                    }
                }
            ]
        })

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": json.dumps(result)
        })

        final_response = get_conversarion(messages)
        return {"reply": final_response.choices[0].message.content}

    else:
        return {"reply": message.content}


@app.post("/chat/stream")
def chat_stream(request: ChatRequest):
    messages = [{"role": "user", "content": request.message}]
    response = get_conversarion(messages)
    message = response.choices[0].message

    if message.tool_calls:
        tool_call = message.tool_calls[0]
        function_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        if function_name == "get_weather":
            result = get_weather(**arguments)
        elif function_name == "get_currency":
            result = get_currency(**arguments)
        else:
            return {"error": "unknown function"}

        messages.append({
            "role": "assistant",
            "content": message.content,
            "tool_calls": [
                {
                    "id": tool_call.id,
                    "type": "function",
                    "function": {
                        "name": tool_call.function.name,
                        "arguments": tool_call.function.arguments
                    }
                }
            ]
        })

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": json.dumps(result)
        })

        return StreamingResponse(stream_generator(messages), media_type="text/plain")

    else:
        return StreamingResponse(stream_generator(messages), media_type="text/plain")