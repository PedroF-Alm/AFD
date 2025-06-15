class AFD:

    def __init__(self, estado_inicial, estados_finais, transicoes):
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.transicoes = transicoes

    def processarLinha(self, linha):
        estado = self.estado_inicial
        resultado = ''
        i = 0
        while i < len(linha):
            simbolo = linha[i]
            try:
                estado = self.transicoes[estado][simbolo]
            except:
                if estado in self.estados_finais:
                    resultado += estado + ' '
                    estado = self.estado_inicial
                    i -= 1
                else:
                    return linha[0:i] + '\'' + simbolo + '\' ' + linha[i+1:-1] + f' Símbolo \'{simbolo}\' não reconhecido pelo AFD no estado ({estado})'
            i += 1
        return resultado
    
    def processarArquivo(self, nome_arquivo_entrada):
        with open(nome_arquivo_entrada, 'r') as arquivo_entrada:
            linha = arquivo_entrada.readline()
            saida = ''
            while linha != '':
                saida += self.processarLinha(linha + ' ') + '\n'
                linha = arquivo_entrada.readline()
            return saida[0:-1]
