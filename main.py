import os

# Declaração das Variáveis Globais
opcao = 0
clientes = []
animais = []
adoções = []

# Função para limpar a tela
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para aguardar que o usuário pressione ENTER
def pressione_enter():
    input('Pressione ENTER para continuar...')

# Função para exibir o Logotipo
def show_title():
    print('''
        ███████████ █████                  ███████████           █████                            
        ░█░░░███░░░█░░███                  ░█░░░███░░░█          ░░███                             
        ░   ░███  ░  ░███████    ██████    ░   ░███  ░   ██████  ███████    ██████  █████████████  
            ░███     ░███░░███  ███░░███       ░███     ███░░███░░░███░    ███░░███░░███░░███░░███ 
            ░███     ░███ ░███ ░███████        ░███    ░███ ░███  ░███    ░███████  ░███ ░███ ░███ 
            ░███     ░███ ░███ ░███░░░         ░███    ░███ ░███  ░███ ███░███░░░   ░███ ░███ ░███ 
            █████    ████ █████░░██████        █████   ░░██████   ░░█████ ░░██████  █████░███ █████
            ░░░░░    ░░░░ ░░░░░  ░░░░░░        ░░░░░     ░░░░░░     ░░░░░   ░░░░░░  ░░░░░ ░░░ ░░░░░ 
    ''')

# Função para exibir os menus
def show_menu(menu, opcoes = True):
    global opcao
    menu_line = '+----------------------------+'
    clear_screen()
    show_title()
    print(menu_line)

    if(menu == 'principal'):
        print('| 1. Clientes                |')
        print('| 2. Animais                 |')
        print('| 3. Adoções                |')
        print('| 0. Sair                    |')
    elif(menu == 'clientes'):
        print('| CLIENTE                    |')
        print(menu_line)
        print('| 1. Novo Cliente            |')
        print('| 2. Ver Clientes            |')
        print('| 0. Voltar                  |')
    elif(menu == 'novo_cliente'):
        print('| NOVO CLIENTE               |')
    elif(menu == 'listar_clientes'):
        print('| VER CLIENTES              |')
    elif(menu == 'animais'):
        print('| ANIMAIS                    |')
        print(menu_line)
        print('| 1. Novo Animal           |')
        print('| 2. Ver Animais          |')
        print('| 0. Voltar                  |')
    elif(menu == 'novo_animal'):
        print('| NOVO ANIMAL               |')
    elif(menu == 'listar_animais'):
        print('| VER ANIMAIS               |')
    elif(menu == 'adoção'):
        print('| ADOÇÃO                    |')
        print(menu_line)
        print('| 1. Nova Adoção           |')
        print('| 2. Ver Adoções           |')
        print('| 0. Voltar                  |')
    elif(menu == 'nova_adoção'):
        print('| NOVA ADOÇÃo               |')
    elif(menu == 'listar_adoção'):
        print('| VER ADOÇÕES                |')
    else:
        pass

    print(menu_line)
    if opcoes:
        opcao = input('Escolha a opção desejada: ')

# Função para cadastrar conforme o tipo informado
def cadastrar(tipo):
    if(tipo == 'clientes'):
        codigo = len(clientes) + 1
        nome = input('Digite o nome do cliente: ')
        email = input('Digite o e-mail do cliente: ')
        # Adicionar o cliente à matriz caso não exista
        clientes.append([codigo, nome, email])
    elif(tipo == 'animais'):
        codigo = len(animais) + 1
        nome = input('Digite o nome do animais: ')
        porte = float(input('Digite o porte do animal: '))
        valor = float(input('Digite o valor do animais: '))
        # Adicionar o animal à matriz
        animais.append([codigo, nome, porte, valor])
    elif(tipo == 'adoções'):
        numero = len(adoções) + 1
        clientes = int(input('Digite o código do cliente: '))
        animais = int(input('Digite o código do animal: '))
        porte = float(input('Digite a porte do animal: '))
        # Adicionar a adoção à matriz
        adoções.append([numero, clientes, animais, porte])

# Função para listar conforme o tipo informado
def listar(tipo):
    if(tipo == 'cliente'):
        for clientes in clientes:
            print(f'código {clientes[0]} - {clientes[1]} - {clientes[2]}')
    elif(tipo == 'animais'):
        for animais in animais:
            print(f'código {animais[0]} - {animais[1]} - {animais[2]}')
    elif(tipo == 'adoções'):
        for adoções in adoções:
            print(f'adoções {adoções[0]} - cliente {clientes[adoções[1]-1][1]} - animal {animais[adoções[2]-1][1]} - qtd = {adoções[3]}')
    else:
        print('Não há valores a exibir...')
        pressione_enter()

# Rotina principal (programa executando em loop infinito)
while True:
    show_menu('principal')

    if(opcao == '1'): # Opção "Cliente" do menu principal
        show_menu('cliente')
        if(opcao == '1'): # Opção "Novo Cliente" do menu "Cliente"
            show_menu('novo_cliente', False)
            cadastrar('clientes') 
        elif(opcao == '2'): # Opção "Listar Clientes" do menu "Clientes"
            show_menu('listar_clientes', False)
            listar('clientes')
            pressione_enter()
        elif(opcao == '0'): # Opção "Voltar" do menu ""
            print('VOLTAR')
        else:
            print('Opção inválida...')
    elif(opcao == '2'): # Opção "Animais" do menu principal
        show_menu('animais')
        if(opcao == '1'): # Opção "Novo Animais" do menu "Animais"
            show_menu('novo_animal', False)
            cadastrar('animais') 
        elif(opcao == '2'): # Opção "Listar Clientes" do menu "Animais"
            show_menu('listar_animais', False)
            listar('animais')
            pressione_enter()
        elif(opcao == '0'): # Opção "Voltar" do menu "Animais"
            print('VOLTAR')
        else:
            print('Opção inválida...')
    elif(opcao == '3'): # Opção "Adoções" do menu principal
        show_menu('adoções')
        if(opcao == '1'): # Opção "Nova adoção" do menu "Adoção"
            show_menu('nova_adoção', False)
            cadastrar('adoções') 
        elif(opcao == '2'): # Opção "Listar Adoções" do menu "Adoção"
            show_menu('listar_adoções', False)
            listar('adoção')
            pressione_enter()
        elif(opcao == '0'): # Opção "Voltar" do menu "Adoção"
            print('VOLTAR')
        else:
            print('Opção inválida...')
    elif(opcao == '0'): # Opção "Sair" do menu principal
        break
    else:
        print('Opção inválida! Digite uma opção do menu...')

# Encerramento do programa após sair do loop inifinito
clear_screen()
print('O programa foi encerrado.')
