import streamlit as st 
from PIL import Image

st.title ("Mi primera App")
st.header("En este espacio comienzo a desarrollar habilidades")
st.write("Puedo realizar back y front")
image=Image.open("foto.png")
st.image(image, caption="Interfaces multimodales")
texto=st.text_input("Escribe algo","este es mi texto")
st.write("El texto escrito es", texto)
