from dotenv import load_dotenv
import os
import requests

load_dotenv()

def get_weather(city : str):
    api_key = os.getenv("weather_api")
    url =  f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()
        print(data)

        result = {
            "city" : city,
            "temperature" : data["main"]["temp"],
            "condition" : data["weather"][0]["description"]


        }
        return result
    except Exception as e:
        return {"error" : str(e)}

def get_currency(from_currency : str, to_currency:str):
    api_key = os.getenv("exchange_api")
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"

    try:
        response = requests.get(url)
        data = response.json()
        print(data)

        rate = data["conversion_rates"][to_currency]
        

        result = {
            "from" : from_currency,
            "to" : to_currency,
            "rate" : rate
        }
        return result
    except Exception as e:
        return {"error" : str(e)}


if __name__ == "__main__":
    print(get_weather("karachi"))
    print(get_currency("USD","PKR"))