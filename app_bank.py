'''Crie um aplicativo de banco, onde o usuário possa: Cadastrar seu nome no aplicativo, Deletar seu nome do aplicativo, Entrar no aplicativo, 
Ao entrar no aplicativo, o usuário pode:
Consultar seu saldo (criar uma nova conta o saldo começa com R$ 0,00; a consulta deverá exibir a data da consulta), Depositar valor, Sacar valor, Sair do programa.
'''
# Obter data e hora atual                                                       
from datetime import datetime

# Lista para armazenar usuários e seus saldos
usuarios = []

# Função exibe menu principal
def menu_principal():
    print('\nMenu principal:')
    print('1. Cadastrar usuário')
    print('2. Deletar usuário')
    print('3. Entrar no APP')
    print('4. Sair do APP')

# Função para exibir o menu do usuário
def exibir_menu_usuario():
    print('\nMenu do Usuário:')
    print('1. Consultar saldo')
    print('2. Depositar valor')
    print('3. Sacar valor')
    print('4. Sair da conta')

# Função cadastra usuário
def cadastrar_usuario(nome):
    for usuario in usuarios:
        if usuario['nome'] == nome:
            print('Usuário já cadastrado.')
            return
    usuarios.append({'nome': nome, 'saldo': 0.0})
    print(f'Usuário {nome} cadastrado com sucesso.')

# Função deleta usuário
def deletar_usuario(nome):
    global usuarios
    usuarios = [usuario for usuario in usuarios if usuario['nome'] != nome]
    print(f'Usuário {nome} deletado com sucesso.')

# Função encontra usuário pelo nome
def encontrar_usuario(nome):
    for usuario in usuarios:
        if usuario['nome'] == nome:
            return usuario
    return None

# Função consulta saldo
def consultar_saldo(usuario):
    data_consulta = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    print(f"Saldo de {usuario['nome']}: R$ {usuario['saldo']:.2f} (Consulta realizada em {data_consulta})")

# Função deposita valor
def depositar_valor(usuario, valor):
    usuario['saldo'] += valor
    print(f'Depósito de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {usuario["saldo"]:.2f}')

# Função saca valor
def sacar_valor(usuario, valor):
    if usuario['saldo'] >= valor:
        usuario['saldo'] -= valor
        print(f'Saque de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {usuario["saldo"]:.2f}')
    else:
        print('Saldo insuficiente.')

# Programa principal
if __name__ == '__main__':
    while True:
        menu_principal()
        opcao = input('Escolha uma opção: ')

        match opcao:
            case '1':
                nome = input('Digite o nome do usuário: ')
                cadastrar_usuario(nome)
            case '2':
                nome = input('Digite o nome do usuário: ')
                deletar_usuario(nome)
            case '3':
                nome = input('Digite o nome do usuário: ')
                usuario = encontrar_usuario(nome)
                if usuario:
                    print(f'Bem-vindo, {nome}.')
                    while True:
                        exibir_menu_usuario()
                        opcao_usuario = input('Escolha uma opção: ')
                        match opcao_usuario: 
                            case '1':
                                consultar_saldo(usuario)
                            case '2':
                                valor = float(input('Digite o valor a ser depositado: '))
                                depositar_valor(usuario, valor)
                            case '3':
                                valor = float(input('Digite o valor a ser sacado: '))
                                sacar_valor(usuario, valor)
                            case '4':
                                print('Saindo da conta.')
                                break
                            case _:
                                print('Opção inválida.')
                else:
                    print('Usuário não encontrado.')
            case '4':
                print('Saindo do programa.')
                break
            case _:
                print('Opção inválida.')

                                



                
            