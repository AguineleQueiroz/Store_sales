from store import srvc_mod
from time import sleep


if __name__ == '__main__':
    matriz = list()

    while True:
        opc_usr = srvc_mod.menu()
        if opc_usr == '1':
            while True:
                srvc_mod.cadastrar_vendedor(matriz)
                op = input('Continuar? [s/n] ')
                if op.lower() != 's':
                    break
        elif opc_usr == '2':
            srvc_mod.cadastrar_vendas(matriz)
        elif opc_usr == '3':
            srvc_mod.consultar_vendas(matriz)
        elif opc_usr == '4':
            srvc_mod.cons_venda_total(matriz)
        elif opc_usr == '5':
            srvc_mod.vendedor_do_mes(matriz)
        elif opc_usr == '6':
            srvc_mod.mes_maior_venda(matriz)
        elif opc_usr == '7':
            srvc_mod.listar_vendedores(matriz)
            continue
        elif opc_usr == '8':
            print('saindo', end=' ')
            for i in range(3):
                print('*', end=' ')
                sleep(0.5)
            break
