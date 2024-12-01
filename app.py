import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import requests

# Funzione per inviare email
def send_email(receiver_email, subject, body, attachments):
    sender_email = "tuoemail@gmail.com"  # Inserisci la tua email
    sender_password = "tuapassword"     # Inserisci la tua password

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    for attachment_path in attachments:
        try:
            with open(attachment_path, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename={os.path.basename(attachment_path)}",
                )
                msg.attach(part)
        except FileNotFoundError:
            return f"Errore: file non trovato {attachment_path}"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        return "Email inviata con successo!"
    except Exception as e:
        return f"Errore nell'invio dell'email: {str(e)}"

# Layout con tab per separare le funzionalità
tab1, tab2 = st.tabs(["Genera Design", "Condividi via Email"])

# Tab per la generazione di design
with tab1:
    st.title("AI Design Lab - Generazione di Design")
    prompt = st.text_input("Inserisci il tuo prompt", "Logo minimalista blu e bianco")
    num_variants = st.slider("Seleziona il numero di design", 1, 5, 3)

    design_urls = []
    design_paths = []

    if st.button("Genera"):
        with st.spinner("Generazione in corso..."):
            for i in range(num_variants):
                response = requests.get("https://source.unsplash.com/500x500/?design,art")
                if response.status_code == 200:
                    file_path = f"design_{i+1}.png"
                    with open(file_path, "wb") as f:
                        f.write(response.content)
                    design_urls.append(response.url)
                    design_paths.append(file_path)

            # Mostra i design generati
            for idx, url in enumerate(design_urls, start=1):
                st.image(url, caption=f"Design #{idx}")
                st.download_button(
                    label=f"Scarica Design #{idx}",
                    data=requests.get(url).content,
                    file_name=f"design_{idx}.png",
                    mime="image/png"
                )

# Tab per inviare i design via email
with tab2:
    st.title("Condivisione via Email")
    receiver_email = st.text_input("Inserisci l'email del destinatario")
    subject = st.text_input("Inserisci l'oggetto dell'email", "Il tuo design generato!")
    body = st.text_area("Inserisci il messaggio", "Ecco i design che hai generato con AI Design Lab.")

    if st.button("Genera e Invia via Email"):
        if not design_paths:
            st.error("Genera almeno un design prima di inviare un'email.")
        elif not receiver_email:
            st.error("Inserisci un'email valida.")
        else:
            with st.spinner("Invio in corso..."):
                message = send_email(receiver_email, subject, body, design_paths)
                st.success(message)

        # Pulizia dei file locali
        for path in design_paths:
            if os.path.exists(path):
                os.remove(path)
