import streamlit as st
import requests
import base64
import os

# Directory per salvare le immagini generate
OUTPUT_DIR = "generated_designs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

st.title("AI Design Lab - Beta")
st.subheader("Crea il tuo design con l'intelligenza artificiale")

# Input per il prompt
prompt = st.text_input("Inserisci il tuo prompt", "Logo minimalista blu e bianco")

# Numero di design da generare
num_variants = st.slider("Seleziona il numero di design", 1, 5, 3)

# Livello di complessità
complexity_level = st.slider("Seleziona il livello di complessità", 1, 10, 5)

# Colore principale
main_color = st.color_picker("Seleziona un colore principale", "#0000FF")

# Pulsante per generare
if st.button("Genera"):
    with st.spinner("Generazione in corso..."):
        results = []
        for idx in range(num_variants):
            # Simulazione di una richiesta API
            response = requests.get("https://source.unsplash.com/500x500/?design,art")
            if response.status_code == 200:
                image_path = os.path.join(OUTPUT_DIR, f"design_{idx + 1}.png")
                with open(image_path, "wb") as f:
                    f.write(requests.get(response.url).content)
                results.append(image_path)

        # Mostra i risultati
        for idx, image_path in enumerate(results, start=1):
            st.image(image_path, caption=f"Design #{idx}")
            with open(image_path, "rb") as f:
                st.download_button(
                    label=f"Scarica Design #{idx}",
                    data=f.read(),
                    file_name=f"design_{idx}.png",
                    mime="image/png"
                )

# Divider
st.markdown("---")

# Sezione galleria
st.header("Galleria dei design generati")

# Carica e mostra le immagini salvate
saved_images = [
    os.path.join(OUTPUT_DIR, img)
    for img in os.listdir(OUTPUT_DIR)
    if img.endswith(".png")
]
if saved_images:
    for img_path in saved_images:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.image(img_path, caption=os.path.basename(img_path))
        with col2:
            if st.button("Elimina", key=img_path):
                os.remove(img_path)
                st.experimental_rerun()
else:
    st.info("Non ci sono immagini nella galleria.")
