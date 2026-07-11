weather_tool = {
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current weather for a given city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "Name of the city"
                }
            },
            "required": ["city"]
        }
    }
}

currency_tool = {
    "type": "function",
    "function": {
        "name": "get_currency",
        "description": "Convert currency rate from one currency to another",
        "parameters": {
            "type": "object",
            "properties": {
                "from_currency": {
                    "type": "string",
                    "description": "Currency code to convert from, e.g. USD"
                },
                "to_currency": {
                    "type": "string",
                    "description": "Currency code to convert to, e.g. PKR"
                }
            },
            "required": ["from_currency", "to_currency"]
        }
    }
}



