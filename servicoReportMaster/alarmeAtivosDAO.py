from bancoAlarmesAtivos import BancoAlarmeSQL


class AlarmeAtivoDAO:
    """
    docimstring
    """
# Falha: 26/01/2021 18:57:56,  3750-CL-02, TE3220_047.VAL_PV_OUT, 29.732769012451172, 5, TESTE

    def cadastrarAlarmeAtivo(self, data, nomeClp, tag, valorAtual, valorTrigger, descricao):

        setBD = BancoAlarmeSQL()
        setBD.createTable("AlarmeAtivo", "data date, nomeClp text, tag text, valorAtual text, valorTrigger text, descricao text")
        conn = setBD.getConexao()
        bd = conn.cursor()
        bd.execute(
            f"INSERT INTO AlarmeAtivo (data, nomeClp, tag, valorAtual, valorTrigger, descricao) VALUES (?, ?, ?, ?, ?, ?)",
            (data, nomeClp, tag, valorAtual, valorTrigger, descricao),
        )
        conn.commit()
        conn.close()

    def deletarAlarmeAtivo(self, id):
        setBD = BancoAlarmeSQL()
        conn = setBD.getConexao()
        bd = conn.cursor()
        bd.execute(f"DELETE from AlarmeAtivo WHERE id = {id}")
        conn.commit()
        conn.close()

    def pesquisarAlarmeAtivoClpTag(self, nomeClp, tag):
        setBD = BancoAlarmeSQL()
        conn = setBD.getConexao()
        bd = conn.cursor()
        
        bd.execute(f"SELECT * from AlarmeAtivo WHERE (nomeClp LIKE '{nomeClp}' and tag LIKE '{tag}') ORDER BY Data ASC LIMIT 1")
        query = bd.fetchall()
        conn.close()
        return query

    def pesquisarAlarmeAtivoID(self, id):
        setBD = BancoAlarmeSQL()
        conn = setBD.getConexao()
        bd = conn.cursor()
        bd.execute(f"SELECT * from AlarmeAtivo WHERE id LIKE '%{id}%'")
        query = bd.fetchall()
        conn.close()
        return query

    def pesquisarTodosAlarmeAtivo(self):
        setBD = BancoAlarmeSQL()
        conn = setBD.getConexao()
        bd = conn.cursor()
        bd.execute(f"SELECT * from AlarmeAtivo order by id")
        query = bd.fetchall()
        conn.close()
        return query

    def deletarTabela(self, nomeTabela):
        setBD = BancoAlarmeSQL()
        conn = setBD.dropTable(nomeTabela)
       
