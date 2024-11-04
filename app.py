import os
restaurantes = []#criação de um dicionário.Serve para armazenar mais de uma informaççao sobre a mesma coisa

def exibir_nome():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)

def exibir_opcoes():#funcão para exibis as opçoes de serviço da aplicação
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def voltar_ao_menu():#Fução para retornar ao menu principal
    input('\nDigite "ENTER" para voltar ao menu principal\n')
    main()

def alternar_status():
    exibir_subtitulo('Alternando status do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar ou desativar: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']#inverte o status do restaurante
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante ['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'#ternario
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado') 

    voltar_ao_menu()

def exibir_subtitulo(texto):
    os.system
    print(texto)
    print()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome'] 
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f' - {nome_restaurante} | {categoria} | {ativo}')
    voltar_ao_menu()

def opcao_invalida(): #função para lidar com dados invalidos
    print('Opção inválida!\n')
    voltar_ao_menu()

def cadastro_restaurante():#função de cadastro de restaurante
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome': nome_restaurante, 'categoria':categoria, 'ativo': False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu()

def finalizar_app(): #função para encerrar o programa
    exibir_subtitulo('Finalizando o APP')   

def escolher_opcao():#funcão para escolher uma das opções
    try: #o try tenta fazer tudo que esta dentro dele caso não consiga executa o except
        opcao_escolhida = int (input('Escolha uma opção: ')) # int transforma os valores em inteiros
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastro_restaurante()
        elif opcao_escolhida== 2: #elif é o equivalente a else if
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_status()
        elif opcao_escolhida == 4:
            finalizar_app()
        else: 
            opcao_invalida()
    except: 
        opcao_invalida()

def main(): #funcão principal
    os.system ('cls')
    exibir_nome()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()