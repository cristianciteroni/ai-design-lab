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
    sender_email = "tuoemail@gmail.com"
    sender_password = "tuapassword"

    # Crea il messaggio email
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    # Corpo dell'email
    msg.attach(MIMEText(body, "plain"))

    # Aggiungi allegati
    for attachment_path in attachments:
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={os.path.basename(attachment_path)}",
            )
            msg.attach(part)

    # Invio email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        return "Email inviata con successo!"
    except Exception as e:
        return f"Errore nell'invio dell'email: {str(e)}"

# App Streamlit
st.title("AI Design Lab - Beta")
st.subheader("Condivisione via Email")

# Email input
receiver_email = st.text_input("Inserisci l'email del destinatario")
subject = st.text_input("Inserisci l'oggetto dell'email", "Il tuo design generato!")
body = st.text_area("Inserisci il messaggio", "Ecco i design che hai generato con AI Design Lab.")

# Simula un design generato
design_paths = ["design_1.png", "design_2.png"]  # Sostituire con i file effettivi generati

# Pulsante per inviare l'email
if st.button("Invia via Email"):
    if receiver_email and design_paths:
        with st.spinner("Invio in corso..."):
            message = send_email(receiver_email, subject, body, design_paths)
            st.success(message)
    else:
        st.error("Inserisci un'email valida e genera almeno un design.")
