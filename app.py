import streamlit as st

st.set_page_config(page_title="AI Design Lab", layout="wide")

# Navbar
tabs = st.tabs(["Genera Design", "Condivisione via Email"])

with tabs[0]:
    st.title("AI Design Lab - Generazione di Design")
    st.subheader("Crea il tuo design con l'intelligenza artificiale")

    # Input per il prompt
    prompt = st.text_input("Inserisci il tuo prompt", "Logo minimalista blu e bianco")

    # Slider per il numero di design
    num_variants = st.slider("Seleziona il numero di design", 1, 5, 3)

    # Slider per il livello di complessità
    complexity = st.slider("Seleziona il livello di complessità", 1, 10, 5)

    # Palette di colori
    primary_color = st.color_picker("Seleziona un colore principale", "#0000FF")

    # Stile
    style = st.selectbox("Seleziona lo stile", ["Minimalista", "Astratto", "Vintage", "Moderno", "Futuristico"])

    # Pulsante per generare
    if st.button("Genera"):
        with st.spinner("Generazione in corso..."):
            results = []
            for _ in range(num_variants):
                try:
                    # URL placeholder per immagini di esempio
                    placeholder_url = f"https://via.placeholder.com/500?text={prompt}+{style}+{primary_color}"
                    results.append(placeholder_url)
                except Exception as e:
                    st.error(f"Errore durante la generazione delle immagini: {e}")

            # Mostra i risultati
            st.subheader("Galleria dei design generati")
            for idx, url in enumerate(results, start=1):
                st.image(url, caption=f"Design #{idx}")
                st.download_button(
                    label=f"Scarica Design #{idx}",
                    data=f"Placeholder per {prompt}".encode(),
                    file_name=f"design_{idx}.txt",
                    mime="text/plain"
                )

with tabs[1]:
    st.title("Condivisione via Email")
    st.subheader("Invia i tuoi design via email")

    # Form email
    receiver_email = st.text_input("Inserisci l'email del destinatario")
    subject = st.text_input("Inserisci l'oggetto dell'email", "Ecco i tuoi design generati!")
    message = st.text_area("Inserisci il messaggio", "Ciao, ecco i tuoi design generati con AI Design Lab!")

    # Pulsante per invio email
    if st.button("Genera e Invia via Email"):
        if receiver_email and "@" in receiver_email:
            st.success(f"Email inviata con successo a {receiver_email}!")
        else:
            st.error("Inserisci un'email valida.")
