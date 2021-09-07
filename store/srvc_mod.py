from itertools import zip_longest
from copy import deepcopy


def titulo_tarefa(titulo):
    print('-' * 42)
    print(titulo.center(42))
    print('-' * 42)


def menu():
    titulo_tarefa(titulo='SERVIÇOS')
    print(
        """        [1] - Cadastrar Vendedor
        [2] - Cadastrar Vendas
        [3] - Consultar Vendas
        [4] - Consultar Total de Vendas
        [5] - Vendedor do Mês
        [6] - Mês com mais Vendas
        [7] - Listar Vendedores
        [8] - Sair """
    )
    print('-' * 42)
    while True:
        opc = input('Operação: ')
        if not opc.isdigit():
            print('\033[31mErro: Código de operação inválido.\033[0;0m')
            opc = input('Operação: ')
        break
    return opc


def cadastrar_vendedor(matriz_dados):
    titulo_tarefa(titulo='NOVO REGISTRO')
    dic_venda = {'01': [], '02': [], '03': [], '04': [], '05': [], '06': [],
                 '07': [], '08': [], '09': [], '10': [], '11': [], '12': []}

    nome = input('\nNome do vendedor: ')

    cod = input('Código do vendedor: ')
    if not cod.isdigit():
        print('\33[31mErro: Código deve conter apenas dígitos\033[0;0m')
        cod = input('Código do vendedor: ')

    venda = deepcopy(dic_venda)
    matriz_dados.append([nome, cod, venda])


def cadastrar_vendas(matrix):
    titulo_tarefa(titulo='REGISTRAR NOVA VENDA')
    busca = False
    while True:
        id_vendedor = input('Código do Vendedor: ')
        mes_venda = input('Mês da Venda [ex:"01"]: ')
        valor = float(input('Valor da venda [0.00]: '))

        for vd in matrix:
            if id_vendedor == vd[1]:
                busca = True
                vd[2][mes_venda].append(valor)

        if not busca:
            print('Não existe vendedor com este código na empresa!')
            continue

        opc = input('Inserir outra Venda? [s/n] ')
        if opc.lower() != 's':
            break


def consultar_vendas(matrix):
    titulo_tarefa(titulo='VENDAS DO MÊS DO FUNCIONÁRIO')
    busca_vendedor = False
    while True:
        cod_vendedor = input('\nCódigo do vendedor: ')
        mes = input('Mês número:[ex: "01"] ')

        for vendedor in matrix:
            if cod_vendedor == vendedor[1]:
                busca_vendedor = True
                for meses, vendas_mes in vendedor[2].items():
                    if meses == mes:
                        if len(vendas_mes) != 0:
                            print(vendas_mes)
                        else:
                            print('\033[31mSem vendas neste mês!\033[0;0m')
        if not busca_vendedor:
            print('\033[31mNão existe vendedor com este código na empresa!\033[0;0m')
            continue

        opc = input('Nova Consulta? [s/n] ')
        if opc.lower() != 's':
            break


def cons_venda_total(matrix):
    titulo_tarefa(titulo='VENDA TOTAL DO FUNCIONÁRIO')
    busca_vendedor = True
    while True:
        cod_vendedor = input('Código do funcionário: ')
        soma_vendas = 0.0
        for vendedores in matrix:
            if cod_vendedor == vendedores[1]:
                busca_vendedor = True
                for meses, vendas_mes in vendedores[2].items():
                    soma_vendas += sum(vendas_mes)

        if not busca_vendedor:
            print('\033[31mNão existe vendedor com este código na empresa!\033[0;0m')
            continue

        print(f'Total de vendas: {soma_vendas}')

        opc = input('Nova Consulta? [s/n] ')
        if opc.lower() != 's':
            break


def vendedor_do_mes(matrix):
    titulo_tarefa(titulo='VENDEDOR DO MÊS')
    while True:
        # cod_vendedor = input('\nCódigo do vendedor: ')
        mes = input('Mês número:[ex: "01"] ')
        maior = 0
        nome_vendedor = ''
        for vendedor in matrix:
            if maior < sum(vendedor[2][mes]):
                maior = sum(vendedor[2][mes])
                nome_vendedor = vendedor[0]
        if maior == 0:
            print('Sem vendas neste mês!')
        else:
            print(f'Vendedor do mês: {nome_vendedor}')
            print(f'Vendeu R${maior} em mercadorias!')

        opc = input('Nova Consulta? [s/n] ')
        if opc.lower() != 's':
            break


def mes_maior_venda(matrix):
    titulo_tarefa(titulo='MÊS COM MAIS VENDAS')
    resultado = {}

    for vendedores in matrix:
        for chave_mes, lista_vendas in vendedores[2].items():
            # Se o mes está no dicionário
            if resultado.get(chave_mes):
                # unindo as listas de vendas dos vendedores
                resultado_temp = zip_longest(resultado.get(chave_mes), lista_vendas, fillvalue=0)

                # soma das listas unidas anteriormente
                soma_temp = []
                for soma in resultado_temp:
                    soma_temp.append(sum(soma))

                # atribuição da soma das listas a um mes
                resultado[chave_mes] = soma_temp
            else:
                resultado[chave_mes] = lista_vendas

    mais_vendas = 0
    mes_mais_venda = ''
    for mes, vendas_totais in resultado.items():
        qtd_vendas = len(vendas_totais)
        if mais_vendas < qtd_vendas:
            mais_vendas = qtd_vendas
            mes_mais_venda = mes
    if mais_vendas == 0:
        print('\033[31mSem registro de vendas!\033[0;0m')
    else:
        print(f'O mês em que foram realizadas mais vendas foi o mês {mes_mais_venda} com {mais_vendas} vendas!')


def listar_vendedores(matrix):
    titulo_tarefa(titulo='REGISTRO DE VENDEDORES')
    if len(matrix) != 0:
        for vendedor in matrix:
            print(vendedor)
    else:
        print('Não há vendedores cadastrados!')

