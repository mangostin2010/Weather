import requests
import json
import streamlit as st
from streamlit_js_eval import get_geolocation
from geopy.geocoders import Nominatim
from PIL import Image
from streamlit_extras.stylable_container import stylable_container

icon = Image.open('clouds-and-sun.png')
st.set_page_config(page_title='Weather', page_icon=icon)

location = get_geolocation()
try:
    latitude = location['coords']['latitude']
    longitude = location['coords']['longitude']
    geoLoc = Nominatim(user_agent='GetLoc')
    locname = geoLoc.reverse((latitude, longitude), language='en')

    # Extract city information
    city = locname.raw.get('address', {}).get('city', 'City not found')

except TypeError:
    #st.success('Please wait. You location information is getting.')
    city = '수원시'


st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)

st.title('Weather')
st.divider()

def option():
    option = st.selectbox(
        '나라를 선택',
        ('Korea / Suwon', 'Philippines / Tacloban'))

    if option == "Korea / Suwon":
        city = "수원시" #도시
    elif option == "Philippines / Tacloban":
        city = "Tacloban"

apiKey = "714b1ecad9eaa65fbd2818d147b3bc89"
lang = 'kr' #언어
units = 'metric' #화씨 온도를 섭씨 온도로 변경
api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={lang}&units={units}"
#weather = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}'

result = requests.get(api)
result = json.loads(result.text)

# name = result['name']
weather = result['weather'][0]['description']
temperature = result['main']['temp']
wind = result['wind']['speed']
humidity = result['main']['humidity']

def weather_single():
    with stylable_container(
        key="container_with_border",
        css_styles="""
            {
                padding: 2.5% 0% 2.5% 7%;


                background: rgba(255, 255, 255, 0.4);
                border-radius: 16px;
                box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
                backdrop-filter: blur(5px);
                -webkit-backdrop-filter: blur(5px);
                border: 1px solid rgba(255, 255, 255, 0.3);
            }
            """,
    ):
        st.metric('날씨', weather)

#col1, col2, col3, col4 = st.columns(4)

with stylable_container(
    key='dddffdfdfdf',
    css_styles="""
        {
            padding: 2.5% 0% 2.5% 7%;
            background: rgba(255, 255, 255, 0.4);
            border-radius: 16px;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(5px);
            -webkit-backdrop-filter: blur(5px);
            border: 1px solid rgba(255, 255, 255, 0.3);
        }
"""
    ):
        st.metric('날씨', weather)

with stylable_container(
    key='dddffdfdfdf',
    css_styles="""
        {
            padding: 2.5% 0% 2.5% 7%;
            background: rgba(255, 255, 255, 0.4);
            border-radius: 16px;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(5px);
            -webkit-backdrop-filter: blur(5px);
            border: 1px solid rgba(255, 255, 255, 0.3);
        }
"""
    ): st.metric("온도", f"{temperature} °C")


with stylable_container(
    key='dddffdfdfdf',
    css_styles="""
        {
            padding: 2.5% 0% 2.5% 7%;
            background: rgba(255, 255, 255, 0.4);
            border-radius: 16px;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(5px);
            -webkit-backdrop-filter: blur(5px);
            border: 1px solid rgba(255, 255, 255, 0.3);
        }
"""
    ):  st.metric("바람", f"{wind} m/s")

with stylable_container(
    key='dddffdfdfdf',
    css_styles="""
        {
            padding: 2.5% 0% 2.5% 7%;
            background: rgba(255, 255, 255, 0.4);
            border-radius: 16px;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(5px);
            -webkit-backdrop-filter: blur(5px);
            border: 1px solid rgba(255, 255, 255, 0.3);
        }
"""
    ):st.metric("습기", f"{humidity}%")

