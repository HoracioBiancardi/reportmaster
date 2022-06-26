import datetime, time, shutil
import smtplib
from email.message import EmailMessage

ano = 2021  # formato AAAA
mes = 1  # usar numeros
dia = 1

diaLimite = 30

deEmailEnd = "sistemas_ta@ferroport.com.br"
paraEmailEnd = "horacio.biancardi@ferroport.com.br"
sender_pass = None
diretorio = None

#'smtp.gmail.com', 587
ipServerSmtp = "10.27.1.9"
portaServerSmtp = 25

dataPadrao = datetime.date(ano, mes, dia)
while True:
    hoje = datetime.date.today()
    delta = hoje - dataPadrao
    print(delta.days)
    if delta.days == (diaLimite - 10):
        enviarEmail(10)

    if delta.days == (diaLimite - 5):
        enviarEmail(5)

    if delta.days == diaLimite:
        enviarEmail(0)
        shutil.rmtree(diretorio)

    time.sleep(3600)


def enviarEmail(diaLimite):
    msg = EmailMessage()
    msg.set_content(
        "Falta {diaLimite} dias para encerrar o uso.\n Favor Renovar a licença."
    )

    msg["Subject"] = "Informação do Server"
    msg["From"] = deEmailEnd
    msg["To"] = paraEmailEnd

    with smtplib.SMTP(ipServerSmtp, portaServerSmtp) as smtp:
        smtp.starttls()
        smtp.login(deEmailEnd, sender_pass)
        smtp.send_message(msg)
