import requests
import json
import streamlit as st


option = st.selectbox(
    '나라의 날씨',
    ('Korea / Suwon', 'Philippines / Tacloban'))

if option == "Korea / Suwon":
    city = "Suwon" #도시
elif option == "Philippines / Tacloban":
    city = "Tacloban"

apiKey = "714b1ecad9eaa65fbd2818d147b3bc89"
lang = 'kr' #언어
units = 'metric' #화씨 온도를 섭씨 온도로 변경
api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={lang}&units={units}"

result = requests.get(api)
result = json.loads(result.text)

name = result['name']
weather = result['weather'][0]['description']
temperature = result['main']['temp']
wind = result['wind']['speed']
humidity = result['main']['humidity']

col1, col2, col3 = st.columns(3)
col1.metric("온도", temperature)
col2.metric("바람", wind)
col3.metric("습기", humidity)
