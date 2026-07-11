# Weather + Currency Bot

A FastAPI backend that uses Groq (Llama 3.3 70B) to answer weather and currency conversion queries through **function calling** and **streaming responses**.

## Features

- **Function Calling**: The AI decides which tool to call based on the user's message — weather lookup or currency conversion.
- **Streaming**: Final responses are streamed back token-by-token for a real-time, typewriter-style experience.
- **Two-call pattern**: First call lets Groq decide on a tool call; the tool result is fed back in a second call to generate the final natural-language answer, streamed to the client.

## Tech Stack

- FastAPI
- Groq API (Llama 3.3 70B)
- OpenWeatherMap API (weather data)
- ExchangeRate-API (currency conversion)

## Project Structure

```
weather-currency-bot/
├── main.py           # FastAPI app + /chat endpoint (tool calling + streaming)
├── tools.py           # get_weather() and get_currency() — external API calls
├── groq_client.py      # Groq client setup, chat + streaming functions
├── schemas.py          # Tool schemas (JSON Schema format) + Pydantic request models
├── .env                # API keys (not committed)
├── requirements.txt
└── README.md
```

## Setup

1. Clone the repo and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file in the root directory:
   ```
   groq_api_key=your_groq_api_key
   weather_api=your_openweathermap_api_key
   exchange_api=your_exchangerate_api_key
   ```

3. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

4. Test the `/chat` endpoint (e.g. via Swagger docs at `/docs`, or Postman for the full streaming effect):
   ```json
   {
     "message": "What's the weather in Karachi?"
   }
   ```

## How It Works

1. User sends a message to `/chat`.
2. Groq is called with the message and the available tool schemas (`get_weather`, `get_currency`).
3. If Groq decides a tool is needed, the matching Python function runs against the real API (OpenWeatherMap or ExchangeRate-API).
4. The tool result is appended to the conversation and sent back to Groq.
5. Groq's final answer is streamed back to the client in real time.

## Notes

- If no tool call is needed (e.g. general conversation), the response is still streamed directly.
- Built as part of an AI Integration learning roadmap — following Structured Output and preceding RAG.
