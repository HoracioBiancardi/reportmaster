import sqlite3
from sqlite3 import Error
import sys
from pathlib import Path
from utils.log import Mylog

logger = Mylog(__name__).getmylogger()


class BancoAlarmeSQL:
    def getConexao(self):
        try:
            self.caminho = str(Path(__file__).parent.absolute())
            conexao = sqlite3.connect(f"{self.caminho}\\reportmasterDBAlarme.db3")
            return conexao
        except Error as e:
            logger.error(e)

    def createTable(self, nomeTabela, variaveis):
        try:
            setBD = self.getConexao()
            c = setBD.cursor()
            c.execute(
                f"CREATE TABLE if not exists {nomeTabela} (\
                    id integer primary key autoincrement,\
                    {variaveis})"
            )
            setBD.commit()
            setBD.close()

            #logger.info(f"Criado a tabela: {nomeTabela}")
        except Error as e:
            logger(e)

    def dropTable(self, nomeTabela):
        try:
            setBD = self.getConexao()
            c = setBD.cursor()
            c.execute(f"DROP TABLE IF EXISTS {nomeTabela}")
            setBD.commit()
            setBD.close()
            logger.info(f"Apagado a tabela: {nomeTabela}")
        except Error as e:
            logger.error(e)


if __name__ == "__main__":
    app = BancoSQL()
    app.createTable("teste", "nome text, sobrenome text")
    app.dropTable("teste")
