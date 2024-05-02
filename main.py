import streamlit as st
import requests

api_key = "HHTXpiVV7tlCENJRjVPEaNj1wF6xbnRUgeUW5vVi"
api_url = "https://api.nasa.gov/planetary/apod?" \
          f"api_key={api_key}"

response = requests.get(api_url)
content = response.json()

image_url = content["url"]
title = "ASTRONOMICAL IMAGE OF THE DAY"

image_response = requests.get(image_url)
image_content = image_response.content

with open("image.png", "wb") as file:
    file.write(image_content)

st.title(title)
st.header(content["title"])
st.title(" ")
st.image("image.png")
st.title(" ")
st.subheader("Description:")
st.write(content["explanation"])