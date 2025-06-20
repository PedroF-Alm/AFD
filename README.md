# AFD

Analisador Léxico Simplificado baseado em um Autômato Finito Determinístico

O algoritmo reconhece tokens, que são identificadores unicos definidos durante o desenvolvimento de uma linguagem de programação e tem como objetivo facilitar o
desenvolvimento da próxima etapa do compilador.
O alisador foi divido em três arquivos mantendo o código limpo e permitindo modificações específicas em um determinado arquivo sem afetar o restante do projeto.

Abaixo especificamos os arquivos e suas respectivas funcionalidades:

 main.py:
>Arquivo principal que recebe e lê um arquivo de entrada fornecido por parâmentro no terminal 
>O arquivo main.py lê o arquivo de configuração (config.jason) e através da função json.loads() decodifica o arquivo config.jason, pegando uma string no formato jason e transformando em um objeto python
> Após fazer a leitura do arquivo jason, o algoritmo pega os valores associados às chaves de estado_inicial, estados_finais e transições e os guarda.
> Com os valores guardados o algoritmo cria uma instância da classe AFD passando todas as configurações pra ele
> Em afd.processarArquivo(sys.argv[1]) o algoritmo recebe o arquivo passado no terminal, lê o arquivo linha por linha e processa de acordo com as configurações especificadas em config.jason e guarda o resultado na variável saída e em seguida imprime no terminal
> O algoritmo tem oferece a possibilidade de gravar saída em um arquivo txt caso seja passado um segundo argumento no trminal

config.json:
> Arquivo para configuração do AFD no formato JSON. O arquivo contém os dados de configuração
do autômato, como seus estados e transições.
No config.json estão definidos:
 - estado_inicial : O estado de onde o AFD sempre começa a processar uma nova sequência de caracteres.
 - estados_finais : Uma lista de estados que se alcançados no final de uma sequência de
entrada indicam que um token válido foi reconhecido
 - transicoes : Um objeto mostra o comportamento do AFD. Cada chave representa um estado atual, e seu valor é outro objeto que mapeia símbolos de entrada para os próximos estados. Essas transições definem como o AFD se move de um estado para outro com base nos caracteres lidos

afd.py:
>Arquivo que contém a implementação da classe AFD  
Funções da classe AFD:
- __init__(self, estado_inicial, estados_finais, transicoes):
>Construtor da classe: inicializa uma nova instância do AFD com o estado inicial, a lista de estados finais e as regras de transição fornecidas

-processarLinha(self, linha):
>Processa uma linha de texto, caractere por caractere e identifica os tokens presentes na linha >O método começa no estado_inicial e, para cada caractere da linha, tenta encontrar uma transição válida. Se uma transição leva a um estado_final, um token é reconhecido, e o AFD é resetado para o estado_inicial para continuar a busca por novos tokens na mesma linha. Se um caractere não tiver uma transição definida para o estado atual, ele retorna um erro. Ela retorna uma string contendo os tokens reconhecidos separados por espaço ou uma mensagem de erro se um simbolo não for reconhecido

-processarArquivo(self, nome_arquivo_entrada) :
>Processa o arquivo de texto, lê o arquivo linha por linha e utiliza o método processarLinha
para analisar cada uma delas
>O método abre o arquivo de entrada, lê cada linha e a passa para processarLinha . O resultado de cada linha é guardado e em seguida o resultado completo do processamento do arquivo é retornado.
