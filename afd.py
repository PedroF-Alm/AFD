class AFD:

    def __init__(self, estado_inicial, estados_finais, transicoes):
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.transicoes = transicoes

    def processarLinha(self, linha):
        estado = self.estado_inicial
        resultado = ''
        for i in linha:
            try:
                estado = self.transicoes[estado][i]
            except:
                return f'Símbolo \'{i}\' não reconhecido pelo AFD no estado ({estado})'
            if estado in self.estados_finais:
                resultado += estado + ' '
                estado = self.estado_inicial
        return resultado
    
    def processarArquivo(self, nome_arquivo_entrada):
        with open(nome_arquivo_entrada, 'r') as arquivo_entrada:
            linha = arquivo_entrada.readline()
            saida = ''
            while linha != '':
                saida += self.processarLinha(linha) + '\n'
                linha = arquivo_entrada.readline()
            return saida[0:len(saida)-1]
