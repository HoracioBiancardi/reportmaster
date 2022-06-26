import configparser
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.absolute()))
# EMAIL_ADDRESS = "sistemas.ferroport.ta@gmail.com"
# EMAIL_PASSWORD = "IHM123ihm!@#"
# EMAIL_SMTP_SERVER = "smtp.gmail.com"
# EMAIL_PORT = 465

# TODO: acresentar no arquivo de configuração o sms se for implementado.
# sms ativado serial port com3 baudrate 460800 timeout:5
from utils.log import Mylog

logger = Mylog(__name__).getmylogger()
class MyConfigWrite:
    def myConfigWrite(self):
        try:
            self.config = configparser.ConfigParser()
            self.config["myEmail"] = {
                "fromAddrres": "sistemas.ferroport.ta@gmail.com",
                "smtpServer": "smtp.gmail.com",
                "port": 465,
                "password": "IHM123ihm!@#",
                "tempoEnvio":1,
            }
            with open("config.ini", "w") as configfile:
                self.config.write(configfile)
        except:
             logger.error("Falha na criação do arquivo Config")
            
            

    def myConfigRead():
        self.config = configparser.ConfigParser()
        return self.config.read("config.ini")


if __name__ == "__main__":
    app = MyConfigWrite()
    app.myConfigWrite()
    
