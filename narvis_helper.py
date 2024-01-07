# narvis_helper.py
import requests
import openai
from config import WEATHER_API_KEY, GPT2_API_KEY

class NarvisHelper:
    def __init__(self):
        self.weather_api_key = WEATHER_API_KEY
        self.gpt2_api_key = GPT2_API_KEY
        self.responses = {
            'tanya ai': self.ask_gpt2,
            'cek cuaca': self.check_weather,
            # ... (other features)
        }

    def check_weather(self, city):
        try:
            weather_url = f'http://api.weatherapi.com/v1/current.json?key={self.weather_api_key}&q={city}'
            response = requests.get(weather_url)
            data = response.json()

            if 'error' in data:
                return f"Failed to get weather information for {city}: {data['error']['message']}"
            else:
                temperature = data['current']['temp_c']
                condition = data['current']['condition']['text']
                return f"Current weather in {city}: {temperature}°C, {condition}"
        except requests.RequestException as e:
            return f'Failed to get weather information: {e}'

    def ask_gpt2(self, user_question):
        openai.api_key = self.gpt2_api_key
        gpt2_endpoint = 'https://api.openai.com/v1/engines/text-davinci-003/completions'

        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=user_question,
                max_tokens=150
            )
            answer = response.choices[0].text.strip()
            return answer
        except Exception as e:
            return f'Failed to get answer from GPT-2: {e}'
            
