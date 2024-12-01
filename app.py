import streamlit as st
import requests

# Titolo dell'app
st.title("AI Design Lab - Beta")
st.subheader("Crea il tuo design con l'intelligenza artificiale")

# Prompt utente
prompt = st.text_input("Inserisci il tuo prompt", placeholder="Logo minimalista blu e bianco")

# Bottone per generare
if st.button("Genera"):
    if prompt:
        # API di Hugging Face
        API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3.5-large"
        headers = {"Authorization": "Bearer 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"}

        # Richiesta all'API
        data = {"inputs": prompt}
        response = requests.post(API_URL, headers=headers, json=data)

        # Controllo della risposta
        if response.status_code == 200:
            st.image(response.content, caption="Risultato Generato")
        else:
            st.error("Errore nella generazione dell'immagine.")
    else:
        st.warning("Inserisci un prompt prima di generare!")

