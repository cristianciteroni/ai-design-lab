import streamlit as st
import requests
import base64

st.title("AI Design Lab - Beta")
st.subheader("Crea il tuo design con l'intelligenza artificiale")

# Input per il prompt
prompt = st.text_input("Inserisci il tuo prompt", "Logo minimalista blu e bianco")

# Numero di design da generare
num_variants = st.slider("Seleziona il numero di design", 1, 5, 3)

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
            st.image(url, caption=f"Design #{idx}")
            st.download_button(
                label=f"Scarica Design #{idx}",
                data=requests.get(url).content,
                file_name=f"design_{idx}.png",
                mime="image/png"
            )
