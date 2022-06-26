import smtplib
import imghdr
from email.message import EmailMessage
import configparser

import sys
from utils.log import Mylog

logger = Mylog(__name__).getmylogger()

class MyEmail:
    def __init__(self, fromAddrres, smtpServer, port, password=None):
        self.fromAddrres = fromAddrres
        self.smtpServer = smtpServer
        self.port = port
        self.password = password


    def enviaEmail(self, msghtml, toEmail):
        try:    
            msg = EmailMessage()
            msg["Subject"] = "Relatório de alarmes ReportMaster "
            msg["From"] = self.fromAddrres
            msg["To"] = toEmail

            with open("resemail.html", "r", encoding="utf-8") as f:
                fileHtml = f.read().format(htmlText=msghtml)

            msg.add_alternative(fileHtml, subtype="html")

            with open("ReportMaster.png", "rb") as f:
                file_data = f.read()
                file_type = imghdr.what(f.name)
                file_name = f.name

            msg.add_attachment(
                file_data, maintype="image", subtype=file_type, filename=file_name
            )

            # with open("ControleForce.xlsx", "rb") as f:
            #     file_data = f.read()
            #     file_name = f.name

            # msg.add_attachment(
            #     file_data, maintype="application", subtype="octet-stream", filename=file_name
            # )

        
            if self.password != None:
                with smtplib.SMTP_SSL(self.smtpServer, self.port) as smtp:
                    smtp.login(self.fromAddrres, self.password)
            with smtplib.SMTP(self.smtpServer, self.port) as smtp:
                smtp.send_message(msg)
        except:
            logger.error("Falha no envio do email")

            


# with smtplib.SMTP(10.27.1.9, 25) as smtp:
# EMAIL_ADDRESS = "sistemas.ferroport.ta@gmail.com"
# EMAIL_PASSWORD = "IHM123ihm!@#"
# EMAIL_SMTP_SERVER = "smtp.gmail.com"
# EMAIL_PORT = 465


if __name__ == "__main__":

    config = configparser.ConfigParser()
    config.read("config.ini")

    fromAddrres = config["myEmail"]["fromAddrres"]
    smtpServer = config["myEmail"]["smtpServer"]
    port = config["myEmail"]["port"]
    password = config["myEmail"]["password"]

    app = MyEmail(fromAddrres, smtpServer, port, password)

    app.enviaEmail(
        """<tr>
        <td><b>24/01/21</b></td>
        <td><b>CLP01</b></td>
        <td><b>ChavEmerg</b></td>
        <td><b>Temperatura do cilo</b></td>
        <td><b>1</b></td>
        <td><b>1</b></td>
        </tr>
        """,
        "ca_fe2001@hotmail.com",
    )
