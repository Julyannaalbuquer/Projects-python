import random
import os

print('\nOlá seja bem-vindo(a) ao jogo, sou AVA a inteligencia artcificial do jogo, e estarei aqui jogando junto com você😉! ')
nome = input('Para começar, por favor digite seu nome: ')
print(f'Prazer em conhcecer {nome} ! Vamos começar a jogar?')
input('\nPrecione enter para começar')
os.system('cls')

sair = False
pontos_do_usuario = 0
ponto_da_ava = 0

while sair == False:
    options = ["pedra", "papel" , "tesoura"]
    escolha_do_usuario = input("Escolha uma função pedra, papel, tesoura ou sair: ")
    escolha_da_ava = random.choice(options)
    
    if escolha_do_usuario == "sair" :
        print("Fim de jogo")
        print("Sua pontuação final é "+str(pontos_do_usuario)+" e a pontuação de AVA é " +str(ponto_da_ava))
        print("Obrigada por jogar! Até a próxima👋")
        sair = True

    if escolha_do_usuario == "pedra":
        if escolha_da_ava == "pedra":
            print("Sua escolha é pedra")
            print("A escolha de AVA é pedra")
            print("Deu empate!")
        elif escolha_da_ava == "papel":
            print("Sua escolha é pedra")
            print("A escolha de AVA é papel")
            print("AVA ganhou!")
            ponto_da_ava += 1
        elif escolha_da_ava == "tesoura":
            print("Sua escolha é pedra")
            print("A escolha de AVA é tesoura")
            print("Você ganhou!")
            pontos_do_usuario += 1

    elif escolha_do_usuario == "papel":
        if escolha_da_ava == "pedra":
            print("Sua escolha é papel")
            print("A escolha de AVA é pedra")
            print("Você ganhou!")
            pontos_do_usuario += 1
        elif escolha_da_ava == "papel":
            print("Sua escolha é papel")
            print("A escolha de AVA é papel")
            print("Deu empate!")
        elif escolha_da_ava == "tesoura":
            print("Sua escolha é papel")
            print("A escolha de AVA é tesoura")
            print("AVA ganhou!")
            ponto_da_ava += 1

    elif escolha_do_usuario == "tesoura":
        if escolha_da_ava == "pedra":
            print("Sua escolha é tesoura")
            print("A escolha de AVA é pedra")
            print("AVA ganhou!")
            ponto_da_ava += 1
        elif escolha_da_ava == "papel":
            print("Sua escolha é tesoura")
            print("A escolha de AVA é papel")
            print("Você ganhou!")
            pontos_do_usuario += 1
        elif escolha_da_ava == "tesoura":
            print("Sua escolha é tesoura")
            print("A escolha de AVA é tesoura")
            print("Deu empate")

    elif escolha_do_usuario != "pedra" or escolha_do_usuario != "papel" or escolha_do_usuario != "tesoura" or escolha_do_usuario != "sair":
        print("Escolha inválida!")