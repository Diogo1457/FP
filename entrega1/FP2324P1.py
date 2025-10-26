"""
Projeto nº1 de Fundamentos da Programação
Título: Montanhas e Vales
Número: ist1109293
Nome: Diogo Lobo
"""

# Constantes
ALFABETO = [chr(i) for i in range(65, 91)]

## Erros
ERRO_OBTEM_CADEIA = 'obtem_cadeia: argumentos invalidos'
ERRO_OBTEM_VALE = 'obtem_vale: argumentos invalidos'
ERRO_TERRITORIO_PARA_STR = 'territorio_para_str: argumento invalido'
ERRO_VERIFICA_CONEXAO = 'verifica_conexao: argumentos invalidos'
ERRO_CALCULA_NUMERO_MONTANHAS = 'calcula_numero_montanhas: argumento invalido'
ERRO_CALCULA_NUMERO_CADEIAS_MONTANHA = 'calcula_numero_cadeias_montanhas: argumento invalido'
ERRO_CALCULA_TAMANHO_VALES = 'calcula_tamanho_vales: argumento invalido'


def eh_tuplo_valido_cv(territorio):
    """
    Verifica se o territorio é um tuplo, com o length pertencente [1, 26] - Caminho Vertical
    :param territorio: território
    :return: bool
    """
    return isinstance(territorio, tuple) and (1 <= len(territorio) <= 26)


def eh_num_valido_linha(coluna):
    """
    Verifica se em cada linha só existe o inteiro 0 ou 1
    :param linha: tuplo
    :return: bool
    """
    for posicao in coluna:
        if type(posicao) != int or posicao not in [0, 1]:
            return False
    return True


def eh_tuplo_valido_ch(territorio):
    """
    Verifica se cada coluna (caminho vertical) é um tuplo válido para um caminho horizontal
    :param territorio: território
    :return: bool
    """
    for coluna in territorio:
        tuplo_valido = isinstance(coluna, tuple) and (1 <= len(coluna) <= 99)  # Coluna é tuplo entre [1-99]
        if not tuplo_valido or not eh_num_valido_linha(coluna) or len(territorio[0]) != len(coluna):
            return False
    return True


def eh_territorio(territorio):
    """
    Verifica se o argumento é um território
    :param territorio: território
    :return: bool
    """
    return eh_tuplo_valido_cv(territorio) and eh_tuplo_valido_ch(territorio)


def obtem_ultimo_index_vh(territorio):
    """
    Obtem o index do último caminho vertical e horizontal
    :param territorio:
    :return: (int, int)
    """
    return len(territorio) - 1, len(territorio[0])


def obtem_ultima_intersecao(territorio):
    """
    Retorna a última interseção de um território
    :param territorio: território
    :return: interseção -> tuplo (character, inteiro)
    """
    cv, ch = obtem_ultimo_index_vh(territorio)   # último caminho vertical, último caminho horizontal
    return (ALFABETO[cv], ch)


def eh_intersecao(intersecao):
    """
    Verifica se o argumento é uma intersecao -> tuplo (character, inteiro)
    1 <= inteiro <= 99
    character [A-Z]
    :param intersecao: intersecao
    :return: bool
    """
    if isinstance(intersecao, tuple) and len(intersecao) == 2 and isinstance(intersecao[0], str) and type(intersecao[1]) == int:
        return intersecao[0] in ALFABETO and 1 <= intersecao[1] <= 99
    return False


def eh_intersecao_valida(territorio, intersecao):
    """
    Verifica se uma interseção pertence ao território
    :param territorio: território
    :param intersecao: interseção
    :return: bool
    """
    num_caminhos_verticais = len(territorio)
    num_caminhos_horizontais = len(territorio[0])
    caminhos_verticas_existentes = ALFABETO[0:num_caminhos_verticais:1]
    return num_caminhos_horizontais >= intersecao[1] and intersecao[0] in caminhos_verticas_existentes


def obtem_indexs_intersecao(intersecao):
    """
    Obtem os indexs necessários para selecionar os elementos dos tuplos
    :param intersecao: intersecao
    :return: tuple, (index1, index2), index1 e index2 são inteiros & 0 <= index1 < 25 & 0 <= index2 < 99
    """
    index_letra = ALFABETO.index(intersecao[0])
    index_numero = intersecao[1] - 1
    return (index_letra, index_numero)


def obtem_valor_intersecao(territorio, intersecao):
    """
    Obtem o elemento presente na intersecao
    :param territorio: territorio
    :param intersecao: intersecao
    :return: int
    """
    index_letra, index_numero = obtem_indexs_intersecao(intersecao)
    return territorio[index_letra][index_numero]


def eh_intersecao_livre(territorio, intersecao):
    """
    Verifica se uma interseção é livre
    :param territorio: território
    :param intersecao: interseção
    :return: bool
    """
    return obtem_valor_intersecao(territorio, intersecao) == 0


def obtem_intersecoes_adjacentes(territorio, intersecao):
    """
    Obtem as intersecoes adjacentes (interseções conectadas por um caminho horizontal ou vertical sem outras interseções entre elas)
    :param territorio: territorio
    :param intersecao: interseção
    :return: tuple, interseções adjacentes
    """
    index_letra, index_numero = obtem_indexs_intersecao(intersecao)
    intersecoes_adjacentes = ()
    if index_numero - 1 >= 0:  # Interseção de Baixo
        intersecoes_adjacentes += ((intersecao[0], intersecao[1] - 1),)
    if index_letra - 1 >= 0:  # Interseção da Esquerda
        intersecoes_adjacentes += ((ALFABETO[index_letra - 1], intersecao[1]),)
    if index_letra + 1 < len(territorio): # Interseção da Direita
        intersecoes_adjacentes += ((ALFABETO[index_letra + 1], intersecao[1]),)
    if index_numero + 1 < len(territorio[index_letra]): # Interseção de Cima
        intersecoes_adjacentes += ((intersecao[0], intersecao[1] + 1),)
    return intersecoes_adjacentes


def lista_intersecoes_dict(lista):
    """
    Transforma uma lista de interseções num dicionário
    :param lista: list
    :return: dict
    """
    dicionario_das_intercecoes = dict()  # Novo dicionário
    for intersecao in lista:
        num = intersecao[1]  # Linha da interseção
        if num not in dicionario_das_intercecoes:  # Se não existir associar um tuplo vazio
            dicionario_das_intercecoes[num] = ()
        dicionario_das_intercecoes[num] += (intersecao[0],)
    return dicionario_das_intercecoes


def ordena_intersecoes(tuplo):
    """
    Ordena as interseções de acordo com a ordem de leitura
    :param tuplo: tuple de interseções (intersecao1, intersecao2, ...)
    :return: tuple
    """
    intersecoes_dict = lista_intersecoes_dict(sorted(tuplo))  # Converte o tuplo para um dict
    intersecoes_ordenadas = ()
    i = 0
    for linha in sorted(intersecoes_dict.keys()):
        for coluna in intersecoes_dict[linha]:
            intersecoes_ordenadas += ((coluna, linha),)
    return intersecoes_ordenadas


def coluna_add_string(elemento):
    """
    Retorna o valor que deve ser adicionado à string to territorio
    :param elemento: int, elemento do territorio 0 ou 1
    :return: str
    """
    return ' .' if elemento == 0 else ' X'


def obtem_cont_linha(linha):
    """
    Retorna o número da linha em string com o espaçamento certo
    :param linha: int, número da linha
    :return: str
    """
    space = ' ' if linha <= 9 else ''
    return space + str(linha)


def valida_territorio(territorio, erro):
    """
    Verifica se o argumento territorio é do tipo territorio, se não for, um erro é gerado
    :param territorio: territorio
    :param erro: str
    :return: None
    """
    if not eh_territorio(territorio):
        raise ValueError(erro)


def valida_intersecao(territorio, intersecao, erro):
    """
    Verifica se o argumento intersecao é do tipo intersecao, se não for, um erro é gerado
    :param territorio: territorio
    :param intersecao: intersecao
    :param erro: str
    :return: None
    """
    if not eh_intersecao(intersecao) or not eh_intersecao_valida(territorio, intersecao):
        raise ValueError(erro)


def valida_territorio_intersecao(territorio, intersecao, erro):
    """
    Verifica se os argumentos são válidos territorio, intersecao são do tipo territorio, intersecao, respetivamente,
    se algum não for, um erro é gerado
    :param territorio: territorio
    :param intersecao: intersecao
    :param erro: str
    :return: None
    """
    valida_territorio(territorio, erro)  # Valida território
    valida_intersecao(territorio, intersecao, erro)  # Valida interseção


def territorio_para_str(territorio):
    """
    Recebe um território e devolve a cadeia de caracteres que o representa
    :param territorio: territorio
    :return: str
    """
    valida_territorio(territorio, ERRO_TERRITORIO_PARA_STR)
    colunas_letras = '   ' + ' '.join(ALFABETO[0:len(territorio)])
    territorio_em_string = colunas_letras + '\n'  # Adicionar alfabeto em cima
    for linha in range(len(territorio[0]), 0, -1):
        territorio_em_string += obtem_cont_linha(linha)  # Adiciona o espaçamento certo
        for coluna in range(len(territorio)):
            territorio_em_string += coluna_add_string(territorio[coluna][linha - 1])
        territorio_em_string += (' ' + obtem_cont_linha(linha) + '\n')  # Adiciona o espaçamento certo
    territorio_em_string += colunas_letras  # Adicionar alfabeto em baixo
    return territorio_em_string


def obtem_intersecoes_adjacentes_tipo(territorio, intersecao, livre, tuplo=()):
    """
    Obtem as intersecões adjacentes livres ou obtem as intersecões adjacentes com montanhas a uma interseção,
    que não estejam já no tuplo fornecido
    :param territorio: territorio
    :param intersecao: intersecao
    :param value: bool
    :param tuplo: tuple
    :return: tuple, intersecoes
    """
    intersecoes_adjacentes = obtem_intersecoes_adjacentes(territorio, intersecao)
    intersecoes_adj_livres = ()
    for inter in intersecoes_adjacentes:
        if eh_intersecao_livre(territorio, inter) == livre and inter not in tuplo:
            intersecoes_adj_livres += (inter,)
    return intersecoes_adj_livres


def obtem_todas_intersecoes_tipo(territorio, livre):
    """
    Obtem todas as interseções que são livres ou montanhas
    :param territorio: territorio
    :param livre: bool
    :return: tuple
    """
    ucv, uch = obtem_ultimo_index_vh(territorio)   # último caminho vertical, último caminho horizontal
    intersecoes = ()
    for letra in ALFABETO[0:ucv+1:1]:
        for num in range(1, uch+1):
            intersecao = (letra, num)
            if eh_intersecao_livre(territorio, intersecao) == livre:
                intersecoes += (intersecao,)
    return intersecoes


def obtem_conexao(territorio, intersecao, cadeia, livre, ijv):
    """
    Obtem as interseções que estão em cadeia com a intersecão dada
    :param territorio: territorio
    :param intersecao: intersecao
    :param cadeia: tuple (intersecao, ...)
    :param livre: bool
    :param ijv: tuple(intersecao, ...) - intersecoes já verificadas
    :return: tuple
    """
    inters_adjcantes = obtem_intersecoes_adjacentes(territorio, intersecao)
    for inter in inters_adjcantes:
        if inter not in ijv:
            ijv.append(inter)
            if eh_intersecao_livre(territorio, inter) == livre:
                cadeia += (inter,)
                cadeia = obtem_conexao(territorio, inter, cadeia, livre, ijv)  
    return cadeia


def obtem_cadeia(territorio, intersecao):
    """
    Obtem todas as interseções que estão conetadas a essa interseção (incluindo a própria),
    ordenadas de acordo com a ordem de leitura do território
    :param territorio: territorio
    :param intersecao: intersecao
    :return: tuple
    """
    valida_territorio_intersecao(territorio, intersecao, ERRO_OBTEM_CADEIA)
    livre = eh_intersecao_livre(territorio, intersecao)
    cadeia = obtem_conexao(territorio, intersecao, (intersecao,), livre, [intersecao])
    return ordena_intersecoes(cadeia)


def valida_montanha(territorio, intersecao, erro):
    """
    Verifica se o elemento da interseção é uma montanha, se não for um erro é gerado
    :param territorio: territorio
    :param intersecao: intersecao
    :param erro: str
    :return: None
    """
    if eh_intersecao_livre(territorio, intersecao):
        raise ValueError(erro)


def valida_argumentos_obtem_vale(territorio, intersecao):
    """
    Verifica se os argumento da funçao vale estão corretos, se não um erro é gerado
    :param territorio: territorio
    :param intersecao: intersecao
    :return: None
    """
    valida_territorio_intersecao(territorio, intersecao, ERRO_OBTEM_VALE)
    valida_montanha(territorio, intersecao, ERRO_OBTEM_VALE)


def obtem_vale(territorio, intersecao):
    valida_argumentos_obtem_vale(territorio, intersecao)
    cadeia = obtem_cadeia(territorio, intersecao)
    vale = ()
    for inter in cadeia:
        intersecoes_adj_livres = obtem_intersecoes_adjacentes_tipo(territorio, inter, True, vale)
        vale += intersecoes_adj_livres
    return ordena_intersecoes(vale)


def valida_verifica_conexao(territorio, intersecao1, intersecao2):
    """
    Verifica se os argumentos da função verifica_conexao são válidos
    :param territorio: territorio
    :param intersecao1: intersecao
    :param intersecao2: intersecao
    :return: None
    """
    valida_territorio(territorio, ERRO_VERIFICA_CONEXAO)
    valida_intersecao(territorio, intersecao1, ERRO_VERIFICA_CONEXAO)
    valida_intersecao(territorio, intersecao2, ERRO_VERIFICA_CONEXAO)


def verifica_conexao(territorio, intersecao1, intersecao2):
    """
    Verifica se duas interseções estão conectadas ou não
    :param territorio: territorio
    :param intersecao1: intersecao
    :param intersecao2: intersecao
    :return: bool
    """
    valida_verifica_conexao(territorio, intersecao1, intersecao2)
    cadeia = obtem_cadeia(territorio, intersecao1)
    return intersecao2 in cadeia


def calcula_numero_montanhas(territorio):
    """
    Calcula o número de montanhas num território
    :param territorio: territorio
    :return: int
    """
    valida_territorio(territorio, ERRO_CALCULA_NUMERO_MONTANHAS)
    return len(obtem_todas_intersecoes_tipo(territorio, False)) # Tamanho do tuplo das interseções com montanhas 


def calcula_numero_cadeias_montanhas(territorio):
    """
    Calcula o número de cadeias de montanhas num território
    :param territorio: territorio
    :return: int
    """
    valida_territorio(territorio, ERRO_CALCULA_NUMERO_CADEIAS_MONTANHA)
    intersecoes = obtem_todas_intersecoes_tipo(territorio, False)
    outras_intersecoes = obtem_todas_intersecoes_tipo(territorio, True)
    if len(outras_intersecoes) == 0: # Se não houver interseções livres, o número de cadeias de montanhas é 1
        return 1
    cadeias = []
    for intersecao in intersecoes:
        cadeia = obtem_cadeia(territorio, intersecao)
        if cadeia not in cadeias:
            cadeias.append(cadeia)
    return len(cadeias) # Número de cadeias montanhas


def calcula_tamanho_vales(territorio):
    """
    Calcula o tamanho dos vales
    :param territorio: territorio
    :return: int
    """
    valida_territorio(territorio, ERRO_CALCULA_TAMANHO_VALES)
    intersecoes = obtem_todas_intersecoes_tipo(territorio, False)
    intersecoes_vales = []
    for intersecao in intersecoes:
        vale = obtem_vale(territorio, intersecao)
        for inter in vale:
            if inter not in intersecoes_vales:
                intersecoes_vales.append(inter)
    return len(intersecoes_vales)  # Número de Vales
