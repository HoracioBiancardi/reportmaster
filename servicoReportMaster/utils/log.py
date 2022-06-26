import logging

# logging.basicConfig(
#     filename="example.log",
#     level=logging.DEBUG,
#     format="%(asctime)s %(levelname)s: %(filename)s %(funcName)s %(message)s",
#     datefmt="%m/%d/%Y %I:%M:%S %p",
# )
# logging.debug("This message should go to the log file")
# logging.info("So should this")
# logging.warning("And this, too")
# logging.error("And non-ASCII stuff, too, like Øresund and Malmö")


# Vamos salvar o nosso arquivo de logger no diretório principal, em um subdiretório com o nome da aplicação, no exemplo o easyCir


class Mylog:
    def __init__(self, name):
        self.name = name

    def getmylogger(self):
        self.file_formatter = logging.Formatter(
            "%(asctime)s~%(levelname)s~%(message)s~module:%(module)s~function:%(funcName)s"
        )
        self.console_formatter = logging.Formatter(
            "%(levelname)s: module:%(module)s~function:%(funcName)s -- %(message)s"
        )

        self.file_handler = logging.FileHandler("logfile.log")
        self.file_handler.setLevel(logging.WARN)
        self.file_handler.setFormatter(self.file_formatter)
        self.console_handler = logging.StreamHandler()
        self.console_handler.setLevel(logging.DEBUG)
        self.console_handler.setFormatter(self.console_formatter)

        self.logger = logging.getLogger(self.name)
        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.console_handler)
        self.logger.setLevel(logging.DEBUG)

        return self.logger