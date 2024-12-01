import streamlit as st
import requests

# Impostazioni della pagina
st.set_page_config(page_title="AI Design Lab", layout="wide")

# Aggiornamento del tema
st.markdown("""
    <style>
    body {
        background-color: #f4f7f6; /* Sfondo chiaro */
        color: #333;
    }
    .css-18e3th9 {
        background-color: #ffffff !important;  /* Colore di sfondo dei riquadri */
    }
    .css-1aumxhk {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50; 
        color: white;
        border: none;
        padding: 10px 20px;
        cursor: pointer;
        border-radius: 5px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextInput>label {
        color: #555;
        font-size: 14px;
    }
    .stSelectbox>label {
        color: #555;
        font-size: 14px;
    }
    .stSlider {
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Navbar
tabs = st.tabs(["Genera Design", "Condivisione via Email"])

# Sezione Genera Design
with tabs[0]:
    st.title("AI Design Lab - Generazione di Design")
    st.subheader("Crea il tuo design con l'intelligenza artificiale in pochi click!")

    # Input per il prompt
    prompt = st.text_input("Inserisci il tuo prompt", "Logo minimalista blu e bianco")

    # Slider per il numero di design
    num_variants = st.slider("Numero di design:", 1, 5, 1)

    # Slider per il livello di complessità
    complexity = st.slider("Livello di complessità:", 1, 10, 5)

    # Palette di colori
    primary_color = st.color_picker("Scegli un colore:", "#0000FF")

    # Stile
    style = st.selectbox("Seleziona lo stile:", ["Minimalista", "Astratto", "Vintage", "Moderno", "Futuristico"])

    # Pulsante per generare
    if st.button("Genera Design"):
        with st.spinner("Generazione in corso..."):
            results = []
            for _ in range(num_variants):
                # Simulazione di una richiesta API
                response = requests.get(f"https://source.unsplash.com/500x500/?{prompt}")
                if response.status_code == 200:
                    results.append(response.url)

            # Mostra i risultati
            st.subheader("Galleria dei design generati")
            for idx, url in enumerate(results, start=1):
                st.image(url, caption=f"{prompt} - {style}")
                st.download_button(
                    label=f"Scarica Design #{idx}",
                    data=requests.get(url).content,
                    file_name=f"design_{idx}.png",
                    mime="image/png"
                )

# Sezione Condivisione via Email
with tabs[1]:
    st.title("Condivisione via Email")
    st.subheader("Invia i tuoi design generati ai tuoi colleghi o clienti!")

    # Form email
    receiver_email = st.text_input("Email del destinatario")
    subject = st.text_input("Oggetto dell'email", "I tuoi design generati!")
    message = st.text_area("Messaggio", "Ciao, ecco i tuoi design generati!")

    # Pulsante per invio email
    if st.button("Invia Email"):
        if receiver_email and "@" in receiver_email:
            st.success(f"Email inviata con successo a {receiver_email}!")
        else:
            st.error("Inserisci un'email valida.")
