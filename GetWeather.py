import requests
import json

city = "Seoul" #도시
apiKey = "714b1ecad9eaa65fbd2818d147b3bc89"
lang = 'kr' #언어
units = 'metric' #화씨 온도를 섭씨 온도로 변경
api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={lang}&units={units}"

result = requests.get(api)
result = json.loads(result.text)

name = result['name']
weather = result['weather'][0]['main']
temperature = result['main']['temp']

print(name)
print(weather)
print(temperature)
