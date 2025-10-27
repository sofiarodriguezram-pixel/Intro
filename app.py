import streamlit as st
from PIL import Image

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Mi primera App",
    page_icon="🌸",
    layout="centered"
)

# --- ESTILOS PERSONALIZADOS ---
page_style = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #fff7f3, #f0f4ff, #e7f9f9);
        color: #333333;
    }

    /* Forzar color de los títulos */
    h1, h2, h3 {
        font-weight: 700;
        text-align: center;
        background: -webkit-linear-gradient(45deg, #5c6bc0, #7e57c2, #64b5f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Cuadro de texto */
    input[type="text"] {
        border-radius: 8px;
        border: 2px solid #d0d7ff;
        padding: 6px;
        background-color: #ffffff;
    }

    /* Pie de imagen */
    figcaption {
        font-style: italic;
        color: #666666;
    }
</style>
"""
st.markdown(page_style, unsafe_allow_html=True)

# --- CONTENIDO ---
st.title("Mi primera App")
st.header("En este espacio comienzo a desarrollar habilidades")
st.write("Puedo realizar back y front")

image = Image.open("foto.png")
st.image(image, caption="Interfaces multimodales")

texto = st.text_input("Escribe algo", "este es mi texto")
st.write("El texto escrito es", texto)
