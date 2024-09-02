import os
restaurantes = []#criação de lista

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

def opcao_invalida(): #função para lidar com dados invalidos
    print('Opção inválida!\n')
    input('Aperte a tecla "ENTER" para voltar ao menu principal')
    main()

def cadastro_restaurante():#função de cadastro de restaurante
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_restaurante)#pega o nome informado e coloca na lista
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    input('Digite "ENTER" para voltar ao menu principal')
    main()

def finalizar_app(): #função para encerrar o programa
    os.system('cls') #limpa o terminal quando finaliza
    print('Encerrando o app')

def escolher_opcao():#funcão para escolher uma das opções
    try: #o try tenta fazer tudo que esta dentro dele caso não consiga executa o except
        opcao_escolhida = int (input('Escolha uma opção: ')) # int transforma os valores em inteiros
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastro_restaurante()
        elif opcao_escolhida== 2: #elif é o equivalente a else if
            print('Listar restaurantes')
        elif opcao_escolhida == 3:
            print('Ativir restaurante')
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