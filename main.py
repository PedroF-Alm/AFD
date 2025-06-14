import sys
import json
from afd import AFD

if len(sys.argv) < 2:
    print("Arquivo de entrada não informado.")
    exit(1)

with open('./config.json', 'r') as config:
    config = json.loads(config.read())
    estado_inicial = config['estado_inicial']
    estados_finais = config['estados_finais']
    transicoes     = config['transicoes']
    
    afd = AFD(estado_inicial, estados_finais, transicoes)
    saida = afd.processarArquivo(sys.argv[1])
    print(saida)

    if len(sys.argv) > 2:
        arquivo_saida = open(sys.argv[2], 'w')
        arquivo_saida.write(saida)
        arquivo_saida.close()