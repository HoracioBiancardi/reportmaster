import sched
import json
import sys
from pathlib import Path
from datetime import datetime
import configparser


from utils.pylogix import PLC  # Arquivos da conexão com o CLP
from utils.log import Mylog
from alarmeAtivosDAO import AlarmeAtivoDAO
from myemail import MyEmail

logger = Mylog(__name__).getmylogger()

sys.path.append("..")


###############################################################
# Serviço que vai rodar no windows
##############################################################################################################
def servicoMonitoramento():
    """
    Servico que vai rodar no windows para aquisição de dados e comparação com o cadastrado no
    program do fontend.
    Pega os dados no arquivo dados.json e compara nos clp para verificar e comparar os valores
    """

    app.enter(1, 0, servicoMonitoramento)
    # pega os valores do arquivo dados.json
    with open("dados.json", "r") as json_file:
        dados = json.load(json_file)

    for ips in dados:
        #agrupa todos os tags para enviar tudo de uma vez para cada ip
        #print(ips["ip"])
        listTags=[]       
        for tag in ips["tags"]:
            listTags.append(tag)
        #print(listTags)
 
    # envia para o clp os dados onde o mesmo retorna nos valores dos tags   
        with PLC() as comm:
           comm.IPAddress = ips["ip"]
           tagsResp = comm.Read(listTags)

    # pega o retorno que são varios tags em uma tupla e intera sobre os mesmos           
        for tagResp in tagsResp:
            #print(tagResp.Value)

    # pega o retorno que são varios tags em uma tupla e intera sobre os mesmos
            if tagResp.Value != None or tagResp.TagName != None:
                trigger = ips["tags"][tagResp.TagName][1]
                
                # como tem valores que são booleanos aqui comparamos para podermos
                # comparar com o valor informado no trigger
                # verificar o retorno do clp se tem tipos com isso podemos comparar antes
                if tagResp.Value == False:
                    if trigger == 0:                    
                        dataHora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                        clp = ips['nome']
                        tag = tagResp.TagName
                        valorAtual = tagResp.Value
                        trigger = ips["tags"][tagResp.TagName][1]
                        desc = ips["tags"][tagResp.TagName][0]

                        alarmeAtivo = AlarmeAtivoDAO()
                        alarmeAtivo.cadastrarAlarmeAtivo(dataHora, clp, tag, valorAtual, trigger, desc)
                    
                        #logger.info("Falha: {},  {}, {}, {}, {}, {}".format(dataHora, clp, tag, valorAtual, trigger, desc))

                elif tagResp.Value == True:
                    if trigger == 1:
                        dataHora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                        clp = ips['nome']
                        tag = tagResp.TagName
                        valorAtual = tagResp.Value
                        trigger = ips["tags"][tagResp.TagName][1]
                        desc = ips["tags"][tagResp.TagName][0]

                        alarmeAtivo = AlarmeAtivoDAO()
                        alarmeAtivo.cadastrarAlarmeAtivo(dataHora, clp, tag, valorAtual, trigger, desc)

                        #logger.info("Falha: {},  {}, {}, {}, {}, {}".format(dataHora, clp, tag, valorAtual, trigger, desc))
                    
                # aqui so para todos os outros valores que não são os booleans
                # problema é se os dados forem de outro tipo, ex. string
                elif type(tagResp.Value) == float or type(tagResp.Value) == int:
                    if float(tagResp.Value) >= float(trigger):                    
                        dataHora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                        clp = ips['nome']
                        tag = tagResp.TagName
                        valorAtual = tagResp.Value
                        trigger = ips["tags"][tagResp.TagName][1]
                        desc = ips["tags"][tagResp.TagName][0]

                        alarmeAtivo = AlarmeAtivoDAO()
                        alarmeAtivo.cadastrarAlarmeAtivo(dataHora, clp, tag, valorAtual, trigger, desc)
                    
                        #logger.info("Falha: {},  {}, {}, {}, {}, {}".format(dataHora, clp, tag, valorAtual, trigger, desc))
                    
                    #Falha: 26/01/2021 18:57:56,  3750-CL-02, TE3220_047.VAL_PV_OUT, 29.732769012451172, 5, TESTE
                else:
                    logger.info("Tipo de dados não compativel")


def enviarEmail():
    config = configparser.ConfigParser()
    config.read("config.ini")

    fromAddrres = config["myEmail"]["fromAddrres"]
    smtpServer = config["myEmail"]["smtpServer"]
    port = config["myEmail"]["port"]
    password = config["myEmail"]["password"]
    tempo = 60*int(config["myEmail"]["tempoenvio"])

    
    app.enter(tempo, 1, enviarEmail)
    app.enter(1, 0, servicoMonitoramento)
    # pega os valores do arquivo dados.json
    with open("dados.json", "r") as json_file:
        dados = json.load(json_file)
    for ips in dados:
        alarmeAtivo = AlarmeAtivoDAO()
        clp = str(ips['nome'])
        tags = list(ips["tags"].keys())

        for tag in tags:
            alarmes = alarmeAtivo.pesquisarAlarmeAtivoClpTag(clp, tag)
            if alarmes != []:
                #(1, '07/02/2021 07:54:30', '3750-CL-02', 'TE3220_047.VAL_PV_OUT', '37.2401962280273', '5', 'TESTE')
                data = alarmes[0][1]
                nome = alarmes[0][2]
                tag = alarmes[0][3]
                valorAtual = alarmes[0][4]
                trigger = alarmes[0][5]
                descricao = alarmes[0][6]
                contatos = ips["tags"][alarmes[0][3]][2]

                #print("data:{}, nome:{}, tag:{}, valorAtual:{}, trigger:{}, descricao:{}, contatos:{}".format(data, nome, tag, valorAtual, trigger, descricao, contatos))

                email = MyEmail(fromAddrres, smtpServer, port)

                email.enviaEmail(
                    f"""<tr>
                    <td><b>{data}</b></td>
                    <td><b>{nome}</b></td>
                    <td><b>{tag}</b></td>
                    <td><b>{valorAtual}</b></td>
                    <td><b>{trigger}</b></td>
                    <td><b>{descricao}</b></td>
                    </tr>
                    """,
                    contatos,
                )

    alarmeAtivo.deletarTabela("AlarmeAtivo")
    
            
###############################################################################################################
#                
###############################################################################################################

app = sched.scheduler()
servicoMonitoramento()
enviarEmail()
app.run()
