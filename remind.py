import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# ---- Konfigurácia ----
MINECRAFT_LIVE_DATE = datetime(2025, 9, 22, 19, 0)  # 22. september 2025, 19:00 CET

EMAIL = os.getenv("EMAIL")       # berie sa z GitHub Secrets
PASSWORD = os.getenv("PASSWORD") # berie sa z GitHub Secrets
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
PRIJEMCA = os.getenv("EMAIL")    # pošle ti to na ten istý email

def posli_email(subject, body):
    msg = MIMEMultipart()
    msg["From"] = EMAIL
    msg["To"] = PRIJEMCA
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)

# ---- Kontrola ----
dnes = datetime.now().date()
rozdiel = (MINECRAFT_LIVE_DATE.date() - dnes).days

if rozdiel in [3, 2, 1, 0]:
    subject = f"⏰ Minecraft Live už za {rozdiel if rozdiel > 0 else 'DNEŠOK!'}"
    body = f"Nezabudni! Minecraft Live sa koná {MINECRAFT_LIVE_DATE.strftime('%d.%m.%Y o %H:%M')}."
    posli_email(subject, body)
    print("✅ Email odoslaný")
else:
    print("ℹ️ Dnes netreba posielať pripomienku.")
