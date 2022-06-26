import json

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.absolute()))
from controller.alarmeCTR import AlarmeCTR

from utils.log import Mylog

logger = Mylog(__name__).getmylogger()

class FileDados:
    def criarArquivoConfiguracaoTagJson(self):
        #try:
        memoriaIP = None
        memoriaDadosIPs = None
        menoriaTag= None
        dictDados=list()
        
        
        alarme = AlarmeCTR()
        for tags in alarme.pesquisaTodosTagsAlarme():
            tagsConcatenados = alarme.pesquisaTodosTagsAlarmeConcatenados(
                tags[0], tags[1], tags[2]
            )
        
            contatos = []
              
            for linha in tagsConcatenados:
                #print(linha)
                contatos.append(linha[5])
                concatContato = [
                    tagsConcatenados[0][0],
                    tagsConcatenados[0][1],
                    tagsConcatenados[0][2],
                    tagsConcatenados[0][3],
                    tagsConcatenados[0][4],
                    contatos,
                    ]

                #print(concatContato)

            if concatContato[0] != memoriaIP and concatContato[2]!=menoriaTag:
                memoriaIP =concatContato[0]
                menoriaTag=concatContato[2]

                contTags={concatContato[2]: [concatContato[3], concatContato[4],concatContato[5]] }

                concatTag = {"ip": concatContato[0],
                            "nome": concatContato[1],
                            "tags": contTags }
                #print(concatTag)
                
            elif concatContato[2]!=menoriaTag:
                menoriaTag =concatContato[2]
                concatTag["tags"].update({concatContato[2]: [concatContato[3], concatContato[4],concatContato[5]]})


            if concatContato[0] != memoriaDadosIPs:
                memoriaDadosIPs = concatContato[0]
                dictDados.append(concatTag)
         
           

        print(dictDados)

        with open("dados.json", "w") as json_file:
            json.dump(dictDados, json_file, indent=4)
        #except:
            #logger.error("Falha na criação do arquivo Json")




if __name__ == "__main__":
    app = FileDados()
    app.criarArquivoConfiguracaoTagJson()

