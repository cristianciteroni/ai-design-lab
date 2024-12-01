import streamlit as st
import requests

# Configura il layout della pagina
st.set_page_config(page_title="AI Design Lab", layout="wide")

# Stile personalizzato
st.markdown("""
    <style>
    .css-18e3th9 {
        padding-top: 3rem;
        padding-bottom: 3rem;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stSlider > div {
        background-color: #1e1e1e;
    }
    </style>
    """, unsafe_allow_html=True)

# Navbar con tab
tabs = st.tabs(["Genera Design", "Condivisione via Email"])

# Tab: Genera Design
with tabs[0]:
    st.title("🎨 AI Design Lab - Generazione di Design")
    st.write("Crea il tuo design con pochi click usando l'intelligenza artificiale!")

    # Prompt e opzioni
    col1, col2 = st.columns(2)
    with col1:
        prompt = st.text_input("Inserisci il tuo prompt:", "Logo minimalista blu e bianco")
        style = st.selectbox("Seleziona lo stile:", ["Minimalista", "Astratto", "Vintage", "Moderno", "Futuristico"])
    with col2:
        primary_color = st.color_picker("Scegli un colore:", "#0000FF")
        complexity = st.slider("Livello di complessità:", 1, 10, 5)

    # Numero di design
    num_variants = st.slider("Numero di design:", 1, 5, 3)

    # Pulsante per generare
    if st.button("Genera Design"):
        with st.spinner("Generazione in corso..."):
            results = []
            for _ in range(num_variants):
                response = requests.get("https://source.unsplash.com/random/300x300/?design")
                if response.status_code == 200:
                    results.append(response.url)
                else:
                    results.append(None)

            # Mostra i risultati in griglia
            st.subheader("Galleria dei design generati:")
            cols = st.columns(3)
            for idx, url in enumerate(results):
                if url:
                    with cols[idx % 3]:
                        st.image(url, caption=f"Design #{idx + 1}")
                        st.download_button("Scarica", requests.get(url).content, f"design_{idx + 1}.png")
                else:
                    st.error("Errore durante la generazione dell'immagine.")

# Tab: Condivisione via Email
with tabs[1]:
    st.title("📧 Condivisione via Email")
    st.write("Invia i tuoi design generati ai tuoi colleghi o clienti!")

    receiver_email = st.text_input("Email del destinatario:", "")
    subject = st.text_input("Oggetto dell'email:", "I tuoi design generati!")
    message = st.text_area("Messaggio:", "Ciao, ecco i tuoi design generati!")

    if st.button("Invia Email"):
        if "@" in receiver_email:
            st.success("Email inviata con successo!")
        else:
            st.error("Per favore, inserisci un'email valida.")
