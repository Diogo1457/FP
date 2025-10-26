"""
Projeto nº2 de Fundamentos da Programação
Instituto Superior Técnico
Título do Projeto: Go
Autor: Diogo Lobo
Nº autor: ist1109293
"""


# Constantes

LETRAS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']

# TAD Interseção
def verifica_tamanhos(coluna, linha):
    """
    Verifica se a coluna e a linha são válidas
    :param coluna: str
    :param linha: int
    :return:
    """
    return coluna in LETRAS and (1 <= linha <= 19) # Coluna entre [A-S] e linha entre [1-19]


def cria_intersecao(coluna, linha):
    """
    Cria uma interseção
    :param coluna: str
    :param linha: int
    :return: intersecao
    """
    if not isinstance(coluna, str) or type(linha) != int or not verifica_tamanhos(coluna, linha): # Coluna é string e linha é int e tamanhos válidos
        raise ValueError('cria_intersecao: argumentos invalidos')
    return (coluna, linha)


def obtem_col(intersecao):
    """
    Obtem a coluna de uma interseção
    :param intersecao: intersecao
    :return: str
    """
    return intersecao[0]


def obtem_lin(intersecao):
    """
    Obtem a linha de uma interseção
    :param intersecao: intersecao
    :return: int
    """
    return intersecao[1]


def eh_intersecao(intersecao):
    """
    Verifica se o argumento é uma intersecao
    :param intersecao: universal
    :return: bool
    """
    if isinstance(intersecao, tuple) and len(intersecao) == 2 and isinstance(obtem_col(intersecao), str) and type(obtem_lin(intersecao)) == int:
        ## Verifica se a intersecao é um tuplo com tamanho 2 e a coluna é uma string e a linha é um inteiro
        return verifica_tamanhos(obtem_col(intersecao), obtem_lin(intersecao))  # Verifica se a coluna e linha estão entre os limites permitidos
    return False


def intersecoes_iguais(inter1, inter2):
    """
    Verifica duas interseções são válidas e se são iguais
    :param inter1: universal
    :param inter2: universal
    :return: bool
    """
    return eh_intersecao(inter1) and eh_intersecao(inter2) and inter1 == inter2


def intersecao_para_str(intersecao):
    """
    Converte uma interseção para string
    :param intersecao: intersecao
    :return: str
    """
    return intersecao[0] + str(intersecao[1])  # coluna mais linha em string


def str_para_intersecao(string):
    """
    Converte uma string para intersecao
    :param string: str
    :return: intersecao
    """
    return cria_intersecao(string[0], int(string[1:]))  # Coluna é a posição 0, linha é a posição 1 até ao fim 


def obtem_num_coluna_linha(coluna, linha, limite):
    """
    Obtem o index da coluna
    :param coluna: str
    :param letras: list
    :return: int
    """
    letras_ult_index = LETRAS.index(obtem_col(limite))  # Obtem o index da última letra
    letras = LETRAS[0:letras_ult_index + 1:1]  # Letras possíveis
    return letras.index(coluna), linha - 1, letras


def obtem_intersecoes_adjacentes(intersecao, limite):
    """
    Obtem as intersecoes adjacentes (interseções conectadas por uma linha ou coluna)
    :param intersecao: intersecao
    :param limite: interseção
    :return: tuple, interseções adjacentes
    """
    coluna, linha = obtem_col(intersecao), obtem_lin(intersecao)
    intersecoes_adjacentes = ()
    index_letra, index_numero, letras = obtem_num_coluna_linha(coluna, linha, limite)
    if index_numero - 1 >= 0:  # Interseção de Baixo
        intersecoes_adjacentes += (cria_intersecao(coluna, linha - 1),)
    if index_letra - 1 >= 0:  # Interseção da Esquerda
        intersecoes_adjacentes += (cria_intersecao(letras[index_letra - 1], linha),)
    if index_letra + 1 < len(letras):  # Interseção da Direita
        intersecoes_adjacentes += (cria_intersecao(letras[index_letra + 1], linha),)
    if index_numero + 1 < len(letras): # Interseção de Cima
        intersecoes_adjacentes += (cria_intersecao(coluna, linha + 1),)
    return intersecoes_adjacentes


def ordena_intersecoes(tuplo):
    """
    Ordena as interseções
    :param tuplo: tuple
    :return: tuple
    """
    return tuple(sorted(tuplo, key=lambda inter: (obtem_lin(inter), obtem_col(inter)))) # Por cada inter ordenar primeiro pela linha e depois pela coluna


# Tad Pedra

def cria_pedra_branca():
    """
    Cria uma pedra branca (O)
    :return: pedra
    """
    return {"tipo": "O"}


def cria_pedra_preta():
    """
    Cria uma pedra preta (X)
    :return: pedra
    """
    return {"tipo": "X"}


def cria_pedra_neutra():
    """
    Cria uma pedra neutra (.)
    :return: pedra
    """
    return {"tipo": "."}


def eh_pedra(pedra):
    """
    Verifica se o argumento dado do tipo pedra ou não
    :param pedra: universal
    :return: bool
    """
    # Verifica se é um dict de tamanho 1 em que existe uma key chamada tipo e essa key tem um valor que pode ser "X" ou "O" ou "."
    return isinstance(pedra, dict) and len(pedra) == 1 and list(pedra.keys())[0] == "tipo" and pedra["tipo"] in ["X", "O", "."]


def eh_pedra_branca(pedra):
    """
    Verifica se uma pedra é branca
    :param pedra: pedra
    :return: bool
    """
    return pedra["tipo"] == "O"


def eh_pedra_preta(pedra):
    """
    Verifica se uma pedra é preta
    :param pedra: pedra
    :return: bool
    """
    return pedra["tipo"] == "X"


def pedras_iguais(p1, p2):
    """
    Verifica se duas pedras são válidas e se são iguais
    :param p1: universal
    :param p2: universal
    :return: bool
    """
    return eh_pedra(p1) and eh_pedra(p2) and p1 == p2


def pedra_para_str(pedra):
    """
    Transforma uma pedra numa string que representa o jogador dono da pedra
    :param pedra: pedra
    :return: str
    """
    return pedra["tipo"]


def eh_pedra_jogador(pedra):
    """
    Verifica se a pedra pertence a algum jogador
    :param pedra: pedra
    :return: bool
    """
    return eh_pedra_branca(pedra) or eh_pedra_preta(pedra)

# TAD Goban

def eh_numero_goban_valido(n):
    """
    Verifica se o tamanho do tabuleiro é válido
    :param n: int
    :return: bool
    """
    return type(n) == int and n in [9, 13, 19]  # n é inteiro e é igual a 9, 13 ou 19


def valida_cria_goban_vazio(n):
    """
    Verifica se o n é um número válido para um tabuleiro de goban
    :param n: int
    :return: None
    """
    if not eh_numero_goban_valido(n):
        raise ValueError('cria_goban_vazio: argumento invalido')


def preenche_inters_goban(n, ib=(), ip=()):
    """
    Preenche as interseções do goban como sendo branca, vazia ou preta

    :param n: int
    :param ib: tuple    interseções brancas
    :param ip: list     interseções pretas
    :return: goban

    Se interseção em ib - Pedra Branca
    Se interseção em ip - Pedra Preta
    Se interseção não está em ib nem em ip - Pedra Neutra
    """
    goban = {}
    for letra in LETRAS[0:n:1]:
        for num in range(1, n+1):
            intersecao = cria_intersecao(letra, num)
            if intersecao in ib:  # Se for pedra branca
                goban[intersecao] = cria_pedra_branca()
            elif intersecao in ip:  # Se for pedra preta
                goban[intersecao] = cria_pedra_preta()
            else:  # Se não estiver no tuplo de pedras brancas nem pretas
                goban[intersecao] = cria_pedra_neutra()
    return goban


def cria_goban_vazio(n):
    """
    Cria um goban vazio
    :param n: int
    :return: goban
    """
    valida_cria_goban_vazio(n)  # Levantar erro caso n for inválido
    return preenche_inters_goban(n)  # Preenche todas as inters com pedras neutras


def sao_intersecoes_validas(inters, n, outro_tuplo):
    """
    Valida se um conjunto de interseções são válidas
    :param inters: tuple
    :param n: int
    :param outro_tuplo: tuple
    :return: bool
    """
    if not isinstance(inters, tuple):
        return False
    goban = cria_goban_vazio(n)
    verificadas = ()
    for i in inters:
        # Verifica se cada i é uma interseção e essa é válida e se cada interseção não aparece mais que uma vez e não aparece nos dois tuplos
        if not eh_intersecao(i) or not eh_intersecao_valida(goban, i) or i in verificadas or i in outro_tuplo:
            return False
        verificadas += (i,)
    return True


def valida_cria_goban(n, ib, ip):
    """
    Verifica se os argumentos para criar um goban são válidos
    :param n: int
    :param ib: tuple
    :param ip: tuple
    :return: None
    """
    if not eh_numero_goban_valido(n) or not sao_intersecoes_validas(ib, n, ip) or not sao_intersecoes_validas(ip, n, ib):
        raise ValueError('cria_goban: argumentos invalidos')


def cria_goban(n, ib, ip):
    """
    Cria um goban como as interseções ocupadas
    :param n: int
    :param ib: tuple    interseções brancas
    :param ip: tuple     interseções pretas
    :return: goban
    """
    valida_cria_goban(n, ib, ip)  # Verifica se n, ib e ip são argumentos válidos
    return preenche_inters_goban(n, ib, ip)  # Preenche o goban com pedras, baseando-se nos tuplos ib e ip


def cria_copia_goban(goban):
    """
    Cria uma cópia do goban
    :param goban: goban
    :return: goban
    """
    return goban.copy()


def obtem_ultima_intersecao(goban):
    """
    Obtem a última interseção de um goban (interseção do canto superior direito)
    :param goban: goban
    :return: intersecao
    """
    num_goban = int(len(goban) ** (1/2))  # Cálcula o tamanho das colunas/linhas do goban
    letra = LETRAS[num_goban - 1]  # Última letra do goban
    return cria_intersecao(letra, num_goban)


def obtem_tamanho_goban(goban):
    """
    Obtem o tamanho de um goban, ou seja, obtem o número de colunas ou de linhas
    :param goban:
    :return:
    """
    return obtem_lin(obtem_ultima_intersecao(goban))  #  nº colunas / nº linhas


def obtem_pedra(goban, inter):
    """
    Obtem a pedra que está associada a uma interseção
    :param goban: goban
    :param inter: intersecao
    :return: pedra
    """
    return goban[inter]


def obtem_conexao(goban, intersecao, cadeia, pedra, limite, ijv):
    """
    Obtem as interseções que estão em cadeia com a intersecão dada
    :param goban: goban
    :param intersecao: intersecao
    :param cadeia: tuple (intersecao, ...)
    :param pedra: pedra
    :param limite: int
    :param ijv: tuple(intersecao, ...) - intersecoes já verificadas
    :return: tuple
    """
    inters_adjcantes = obtem_intersecoes_adjacentes(intersecao, limite)  # Inters Adjacentes
    for inter in inters_adjcantes:
        if inter not in ijv:  # Se a interseção não tiver sido anteriormente verificada
            ijv.append(inter)
            if pedras_iguais(obtem_pedra(goban, inter), pedra):  # Verifica se as pedras têm o mesmo tipo
                cadeia += (inter,)
                cadeia = obtem_conexao(goban, inter, cadeia, pedra, limite, ijv)
    return cadeia


def obtem_cadeia(goban, intersecao):
    """
    Obtem todas as interseções que estão conetadas a essa interseção (incluindo a própria)
    ordenadas de acordo com a ordem de leitura do goban, que têm uma pedra com o mesmo tipo
    (livre, branca ou preta) que a pedra colocada na interseção dada
    :param goban: goban
    :param intersecao: intersecao
    :return: tuple
    """
    pedra = obtem_pedra(goban, intersecao)
    limite = obtem_ultima_intersecao(goban)  # Uĺtima interseção do goban
    cadeia = obtem_conexao(goban, intersecao, (intersecao,), pedra, limite, [intersecao])  # Função recursiva para obter cadeia
    return ordena_intersecoes(cadeia)


def coloca_pedra(goban, intersecao, pedra):
    """
    Coloca uma pedra numa interseção do goban
    :param goban: goban
    :param intersecao: intersecao
    :param pedra: pedra
    :return: goban
    """
    goban[intersecao] = pedra
    return goban


def remove_pedra(goban, intersecao):
    """
    Remove uma pedra do goban
    :param goban: goban
    :param intersecao: intersecao
    :return: goban
    """
    goban[intersecao] = cria_pedra_neutra()
    return goban


def remove_cadeia(goban, tuplo):
    """
    Remove uma cadeia de interseções
    :param goban: goban
    :param tuplo: tuple
    :return: goban
    """
    for inter in tuplo:
        goban = remove_pedra(goban, inter)
    return goban


def eh_goban(goban):
    """
    Verifica se o argumento dado é um goban
    :param goban: universal
    :return: bool
    """
    # Verifica se um dicionário com tamanho entra 9²=81, 13²=169, 19²=361
    if isinstance(goban, dict) and len(goban) in [81, 169, 361]:
        for inter in goban:
            # Verifica se as interseções do goban são interseções e se as pedras são pedras
            if not eh_intersecao(inter) or not eh_pedra(obtem_pedra(goban, inter)):
                return False
        return True
    return False


def eh_intersecao_valida(goban, intersecao):
    """
    Verifica se a interseção fornecida existe no goban
    :param goban: goban
    :param intersecao: intersecao
    :return: bool
    """
    return intersecao in goban


def gobans_iguais(g1, g2):
    """
    Verifica se dois gobans são válidos e se são iguais
    :param g1: universal
    :param g2: universal
    :return: bool
    """
    if eh_goban(g1) and eh_goban(g2):
        ultima_intersecao_g1 = obtem_ultima_intersecao(g1)
        ultima_intersecao_g2 = obtem_ultima_intersecao(g2)
        ultima_linha_g1 = obtem_lin(ultima_intersecao_g1)
        ultima_linha_g2 = obtem_lin(ultima_intersecao_g2)
        if ultima_linha_g1 == ultima_linha_g2: # Verifica se o tamanho dos gobans é o mesmo
            for letra in LETRAS[0:ultima_linha_g1:1]:
                for num in range(1, ultima_linha_g1+1):
                    inter = cria_intersecao(letra, num)
                    pedra_g1 = obtem_pedra(g1, inter)
                    pedra_g2 = obtem_pedra(g2, inter)
                    if not pedras_iguais(pedra_g1, pedra_g2):  # Verifica se as pedras do goban são iguais
                        return False
            return True
    return False


def obtem_cont_linha(linha):
    """
    Retorna o número da linha em string com o espaçamento certo
    :param linha: int, número da linha
    :return: str
    """
    space = ' ' if linha <= 9 else ''
    return space + str(linha)


def elemento_add_string(goban, inter):
    """
    Retorna o valor que deve ser adicionado à string do goban
    :param goban: goban
    :param inter: intersecao
    :return: str
    """
    return ' ' + pedra_para_str(obtem_pedra(goban, inter))


def goban_para_str(goban):
    """
    Transforma um goban numa string
    :param goban: goban
    :return: str
    """
    tamanho_goban = obtem_tamanho_goban(goban)
    colunas_letras = '   ' + ' '.join(LETRAS[0:tamanho_goban])
    goban_em_string = colunas_letras + '\n'  # Adicionar alfabeto em cima
    for linha in range(tamanho_goban, 0, -1):
        goban_em_string += obtem_cont_linha(linha)  # Adiciona o espaçamento certo
        for coluna in range(tamanho_goban):
            inter = cria_intersecao(LETRAS[coluna], linha)
            goban_em_string += elemento_add_string(goban, inter)
        goban_em_string += (' ' + obtem_cont_linha(linha) + '\n')  # Adiciona o espaçamento certo
    goban_em_string += colunas_letras  # Adicionar alfabeto em baixo
    return goban_em_string


def obtem_todas_intersecoes_tipo(goban, pedra):
    """
    Obtem todas as interseções possíveis com pedras do mesmo tipo
    :param goban: goban
    :param pedra: pedra
    :return: tuple
    """
    n = obtem_tamanho_goban(goban)   # Número de colunas/linhas do goban
    intersecoes = ()
    for letra in LETRAS[0:n:1]:
        for num in range(1, n+1):
            intersecao = cria_intersecao(letra, num)
            if pedras_iguais(obtem_pedra(goban, intersecao), pedra):  # Verifica se as pedras têm o mesmo tipo
                intersecoes += (intersecao,)
    return intersecoes


def obtem_todas_intersecoes_neutras(goban):
    """
    Obtem todas as interseções neutras do goban
    :param goban: goban
    :return: tuple
    """
    return obtem_todas_intersecoes_tipo(goban, cria_pedra_neutra())


def ordena_territorios(territorios):
    """
    Ordena os territórios de acordo com a primeira interseção do território
    :param territorios: tuple
    :return: tuple
    """
    pri_inters = tuple(t[0] for t in territorios)  # Obtem a primeira interseção de cada território
    ordenadas = ordena_intersecoes(pri_inters)  # Ordena as primeiras interseções
    ters_ordenados = ()
    # Ordena os territórios através da primeira interseção
    for i in ordenadas:
        for t in territorios:
            if intersecoes_iguais(i, t[0]):
                ters_ordenados += (t,)
    return ters_ordenados


def obtem_territorios(goban):
    """
    Obtem todos os territórios do goban
    :param goban: goban
    :return: tuple
    """
    intersecoes = obtem_todas_intersecoes_neutras(goban)  # Todas as interseções com pedras neutras
    cadeias = ()
    intersecoes_verificadas = ()
    for intersecao in intersecoes:
        if intersecao not in intersecoes_verificadas:
            cadeia = obtem_cadeia(goban, intersecao)  # Cadeia de interseções neutras
            if cadeia not in cadeias:
                cadeias += (cadeia,)
                intersecoes_verificadas += tuple(filter(lambda i: i not in intersecoes_verificadas, cadeia))  # Adicionar as interseções da cadeia que não estejam já nas verificadas 
    return ordena_territorios(cadeias)


def intersecao_ocupada(goban, inter):
    """
    Verifica se a interseção está ocupada por uma pedra de algum jogador
    :param goban: goban
    :param inter: intersecao
    :return: bool
    """
    pedra = obtem_pedra(goban, inter)
    return eh_pedra_jogador(pedra)


def obtem_adjacentes_diferentes(goban, tuplo):
    """
    Obtem as interseções adjacentes às interseções do tuplo:
        - que estejam ocupadas se a interseção do tuplo estiver livre
        - que estejam livres se a interseção do tuplo estiver ocupada
    :param goban: goban
    :param tuplo: tuple
    :return: tuple
    """
    limite = obtem_ultima_intersecao(goban)  # Última interseção do goban
    intersecoes = ()
    for inter in tuplo:
        ocupada = intersecao_ocupada(goban, inter)  # Livre ou Ocupada
        inters_adjs = obtem_intersecoes_adjacentes(inter, limite)  # Inters Adjacentes
        for inter_adj in inters_adjs:
            adj_ocupada = intersecao_ocupada(goban, inter_adj)  # Livre ou Ocupada
            if ocupada != adj_ocupada and inter_adj not in intersecoes:
                intersecoes += (inter_adj,)
    return ordena_intersecoes(intersecoes)


def obtem_pedra_contraria(pedra):
    """
    Se a pedra fornecida for uma pedra branca retorna uma pedra preta,
    Se a pedra fornecida for uma pedra preta retorna uma pedra branca,
    Se a pedra fornecida for uma pedra neutra retorna uma pedra neutra

    :param: pedra
    :return: pedra
    """
    if eh_pedra_branca(pedra):
        n_pedra = cria_pedra_preta()
    elif eh_pedra_preta(pedra):
        n_pedra = cria_pedra_branca()
    else:
        n_pedra = pedra
    return n_pedra


def pedras_para_remover(goban, pedra):
    """
    Obtem todas as pedras para remover
    :param goban: goban
    :param pedra: pedra
    :return: tuple
    """
    inters = obtem_todas_intersecoes_tipo(goban, pedra)  # Todas as interseções do tipo da pedra
    sem_liber = ()
    verificadas = ()  # Interseções verificadas
    for i in inters:
        if i not in verificadas:
            cadeia = obtem_cadeia(goban, i)  # Obtem a cadeia de pedras para verificar as liberdades
            verificadas += cadeia
            liberdades = obtem_adjacentes_diferentes(goban, cadeia)
            if liberdades == ():  # Verifica se não tem liberdades
                sem_liber += cadeia
    return sem_liber


def jogada(goban, inter, pedra):
    """
    Faz uma jogada do jogador
    :param goban: goban
    :param inter: intersecao
    :param pedra: pedra
    :return: goban
    """
    goban = coloca_pedra(goban, inter, pedra)
    n_pedra = obtem_pedra_contraria(pedra)  # Obtem a pedra de cor contrária à fornecida
    pedras_remover = pedras_para_remover(goban, n_pedra)
    goban = remove_cadeia(goban, pedras_remover)  # Remove as pedras do outro jogador sem liberdades
    return goban


def obtem_intersecoes_pedras_brancas(goban):
    """
    Obtem todas as interseções com pedras brancas
    :param goban: goban
    :return: tuple
    """
    return obtem_todas_intersecoes_tipo(goban, cria_pedra_branca())


def obtem_intersecoes_pedras_pretas(goban):
    """
    Obtem todas as interseções com pedras pretas
    :param goban: goban
    :return: tuple
    """
    return obtem_todas_intersecoes_tipo(goban, cria_pedra_preta())


def obtem_pedras_jogadores(goban):
    """
    Obtem o número de pedras do jogador branco e do jogador preto
    :param goban: goban
    :return: tuple - (pedras_brancas, pedras_pretas)
    """
    npb = len(obtem_intersecoes_pedras_brancas(goban))  # Número de pedras brancas
    npp = len(obtem_intersecoes_pedras_pretas(goban))  # Número de pedras pretas
    return npb, npp


def calcula_pontos(goban):
    """
    Calcula o número de pontos do jogador branco e do jogador preto
    :param goban: goban
    :return: tuple (pontos_brancas, pontos_pretas)
    """
    pontos_brancas, pontos_pretas = obtem_pedras_jogadores(goban)
    if pontos_brancas == 0 and pontos_pretas == 0:
        return (0, 0)
    territorios = obtem_territorios(goban)
    for t in territorios:
        adjs_difs = obtem_adjacentes_diferentes(goban, t)  # Fronteiras de cada território
        length_terr = len(t)  # Tamanho do território
        if adjs_difs:  # Se existir fronteira
            if all(eh_pedra_branca(obtem_pedra(goban, inter)) for inter in adjs_difs):  # Se todos da fronteira forem brancos território pertence ao jogador branco
                pontos_brancas += length_terr
            elif all(eh_pedra_preta(obtem_pedra(goban, inter)) for inter in adjs_difs): # Se todos da fronteira forem pretos território pertence ao jogador preto
                pontos_pretas += length_terr
    return pontos_brancas, pontos_pretas


def eh_jogada_legal(goban, intersecao, pedra, goban_sec):
    """
    Verifica se uma jogada é possível ou não
    :param goban: goban
    :param intersecao: intersecao
    :param pedra: pedra
    :param goban_sec: goban
    :return: bool
    """
    # Valida se a interseção é válida e se a interseção está livre
    if not eh_intersecao_valida(goban, intersecao) or intersecao not in obtem_todas_intersecoes_neutras(goban):
        return False
    goban_copy = cria_copia_goban(goban)
    goban_copy = jogada(goban_copy, intersecao, pedra)  # Fazer jogada na cópia
    cadeia = obtem_cadeia(goban_copy, intersecao)
    liberdades = obtem_adjacentes_diferentes(goban_copy, cadeia)
    if not liberdades:  # Se algum ficar sem liberdades a jogada é inválida
        return False
    return not gobans_iguais(goban_copy, goban_sec)  # ~(fica igual ao estado anterior)


def obtem_digits(goban):
    """
    Obtem dígitos válidos
    :param goban: goban
    :return: str
    """
    n = obtem_tamanho_goban(goban)  # Tamanho do goban
    return [str(i) for i in range(1, n+1)] # Lista de strings dos dígitos de [1, n]


def turno_jogador(goban, pedra, goban_sec):
    """
    Pede uma jogada ao jogador
    :param goban: goban
    :param pedra: pedra
    :param goban_sec: goban
    :return: bool
    """
    pedra_str = pedra_para_str(pedra)  # Obter Jogador
    digits = obtem_digits(goban)
    while True:
        try:
            value = input(f"Escreva uma intersecao ou 'P' para passar [{pedra_str}]:")  # Pedir Input
            if value == "P":  # Jogador passou
                return False
            inter = str_para_intersecao(value)
        except (ValueError, IndexError):
            continue  # Interseção passada não é válida, pedir nova
        else:
            jogada_legal = eh_jogada_legal(goban, inter, pedra, goban_sec)
            if jogada_legal:  # Verificar se a jogada é válida
                goban = jogada(goban, inter, pedra)
                break
    return True


def valida_intersecao_str(i, letras, digits):
    """
    Valida uma string de uma interseção
    :param i: str
    :param letras: list
    :param digits: list
    :return: bool
    """
    return isinstance(i, str) and len(i) in [2, 3] and i[0] in letras and i[1:] in digits


def valida_go(n, tb, tp):
    """
    Valida os argumentos da função go
    :param n: int
    :param tb: tuple
    :param tp: tuple
    :return: None
    """
    def valida_tuplo_go(letras, digits, tuplo):
        """
        Valida o tuplo passado à função go
        :param letras: list
        :param digits: list
        :param tuplo: tuple
        :return: bool
        """
        if not isinstance(tuplo, tuple):
            return False
        return all(valida_intersecao_str(i, letras, digits) for i in tuplo) # Valida a interseção para string

    if eh_numero_goban_valido(n):  # Tamanho válido do tabuleiro
        digits = obtem_digits(cria_goban_vazio(n))  # Obtem Dígitos Válidos
        letras = LETRAS[0:n] # Obtem letras válidas
        if not valida_tuplo_go(letras, digits, tb) or not valida_tuplo_go(letras, digits, tp):
            raise ValueError('go: argumentos invalidos')
    else:
        raise ValueError('go: argumentos invalidos')


def converte_tuplo_intersecoes_go(tuplo):
    """
    Converte o tuplo recebido pela função go para o tuplo da cria goban
    :param tuplo: tuple
    :return: tuple
    """
    return tuple(map(lambda i: str_para_intersecao(i), tuplo))


def escolhe_tabuleiro_para_criar(n, tb, tp):
    """
    Escolhe o tabuleiro para criar
    :param n: int
    :param tb: tuple
    :param tp: tuple
    :return: goban
    """
    ## Se nenhuma peça for especificada o goban a criar deve ser vazio
    if not tb and not tp:
        return cria_goban_vazio(n)
    else:
        return cria_goban(n, tb, tp)


def display_calcula_pontos(goban):
    """
    Mostra os pontos de cada jogador
    :param goban: goban
    :return: None
    """
    pontos_brancas, pontos_pretas = calcula_pontos(goban)  # Calcula os pontos de cada jogador
    print(f"Branco (O) tem {pontos_brancas} pontos")
    print(f"Preto (X) tem {pontos_pretas} pontos")


def display_go(goban):
    """
    Mostra o tabuleiro de go e os pontos
    :param goban: goban
    :return: None
    """
    display_calcula_pontos(goban)
    print(goban_para_str(goban))


def go(n, tb=(), tp=()):
    """
    Funças principal que permite jogar um jogo completo de go
    :param int: int
    :param tuplo1: tuple
    :param tuplo2: tuple
    :return: bool
    """
    valida_go(n, tb, tp)
    tb, tp = converte_tuplo_intersecoes_go(tb), converte_tuplo_intersecoes_go(tp) 
    try:
        goban = escolhe_tabuleiro_para_criar(n, tb, tp)
    except ValueError:
        raise ValueError('go: argumentos invalidos')
    passou_a_vez = False
    pedra = cria_pedra_preta()  # Jogador Inicial
    goban_anterior_preto = goban.copy()
    goban_anterior_branco = goban.copy()
    display_go(goban)  # Display pontos e goban
    while True:  # Game Play
        pedra_preta = pedras_iguais(pedra, cria_pedra_preta())
        goban_anterior = goban_anterior_preto if pedra_preta else goban_anterior_branco  # Estado do tabuleiro anterior do jogador
        turno = turno_jogador(goban, pedra, goban_anterior)
        display_go(goban)  # Display pontos e goban
        # Atualizar estados anterirores do tabuleiro após a jogada
        if pedra_preta:
            goban_anterior_preto = goban.copy()
        else:
            goban_anterior_branco = goban.copy()
        # Verifica se o jogo acabou
        if not turno:
            if passou_a_vez == True:
                break
            passou_a_vez = True
        else:
            passou_a_vez = False
        pedra = obtem_pedra_contraria(pedra) # Proximo jogador
    pontos_brancas, pontos_pretas = calcula_pontos(goban)
    return pontos_brancas >= pontos_pretas  # Verifica quem ganhou o jogo, retorna True se foi o jogador branco, False se foi o jogador preto

