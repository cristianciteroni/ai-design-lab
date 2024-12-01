import streamlit as st
import requests
import base64
import io
from PIL import Image

st.title("AI Design Lab - Beta")
st.subheader("Crea il tuo design con l'intelligenza artificiale")

# Input per il prompt
prompt = st.text_input("Inserisci il tuo prompt", "Logo minimalista blu e bianco")

# Numero di design da generare
num_variants = st.slider("Seleziona il numero di design", 1, 5, 3)

# Slider per la complessità del design
complexity = st.slider("Seleziona il livello di complessità", 1, 10, 5)

# Colore principale
color = st.color_picker("Seleziona un colore principale", "#0000FF")

# Inizializza galleria
if "gallery" not in st.session_state:
    st.session_state["gallery"] = []

# Pulsante per generare
if st.button("Genera"):
    with st.spinner("Generazione in corso..."):
        results = []
        for _ in range(num_variants):
            # Simulazione di una richiesta API
            response = requests.get("https://source.unsplash.com/500x500/?design,art")
            if response.status_code == 200:
                results.append(response.url)

        # Mostra i risultati
        for idx, url in enumerate(results, start=1):
            # Scarica l'immagine per la galleria
            image_data = requests.get(url).content
            image = Image.open(io.BytesIO(image_data))
            st.session_state["gallery"].append(image)

            # Mostra l'immagine
            st.image(url, caption=f"Design #{idx}")
            
            # Pulsante di download
            st.download_button(
                label=f"Scarica Design #{idx}",
                data=image_data,
                file_name=f"design_{idx}.png",
                mime="image/png"
            )

# Mostra galleria personale
if st.session_state["gallery"]:
    st.header("Galleria dei tuoi design")
    for idx, img in enumerate(st.session_state["gallery"]):
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        st.image(img, caption=f"Design salvato #{idx + 1}")
        st.download_button(
            label=f"Scarica Design #{idx + 1}",
            data=buffer.getvalue(),
            file_name=f"design_saved_{idx + 1}.png",
            mime="image/png"
        )
