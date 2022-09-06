import os
import random
import time

print('=' * 44)
print('Bem vindo ao jogo de Papel, Pedra ou Tesoura') #mensagem boas vindas do jogo
print('=' * 44)
lista_jogo = ['PAPEL','PEDRA','TESOURA'] #opções de jogada para o computador
meu_placar = 0 #variavel para guardar placar de vitórias do jogador
placar_computador = 0 #variavel para guardar placar de vitórias do computador

def inicio_jogo():

    try:
        os.system('cls')
        print('=' * 15)    
        print('PLACAR:') #mostra informações do placar do jogo
        print(f'Você: {meu_placar}') #placar do jogador
        print(f'Computador: {placar_computador}') #placar do computador
        print('=' * 15)
        print('')
        print('Escolha seu lance:') #menu de opções de jogada
        print('0 - PAPEL | 1 - PEDRA | 2 - TESOURA')
        lance = int(input()) #recebe o valor relacionado a opção
        apostar(lance) #envia a opção para ser verificada
    except: #se o usuário digitar uma opção inválida  
        print('Digite uma opção válida')
        time.sleep(1) #espera 1 segundo
        inicio_jogo() #a função é chamada novamente

def apostar(lance): #função faz a verificação dos resultados

    global placar_computador 
    global meu_placar 

    print(f'Sua jogada: {lista_jogo[lance]}') #mostra minha jogada
    computador = random.choice(lista_jogo) # computador sorteia uma opção
    print(f'Jogada do computador: {computador}') # mostra a opção sorteada

    if lance == 0 and computador == 'PAPEL': #faz a verificação do resultado
        print('Resultado: EMPATE') #mostra resultado na tela
        jogar_novamente() #chama a função para o usuário decidir se quer jogar novamente
    elif lance == 0 and computador == 'PEDRA': 
        print('Resultado: VOCÊ VENCEU') 
        meu_placar += 1 #soma +1 no placar a cada vitoria do jogador
        jogar_novamente() 
    elif lance == 0 and computador == 'TESOURA': 
        print('Resultado: VOCÊ PERDEU')
        placar_computador += 1 #soma +1 no placar a cada vitoria do computador
        jogar_novamente() 
    elif lance == 1 and computador == 'PAPEL': 
        print('Resultado: VOCÊ PERDEU') 
        placar_computador += 1 
        jogar_novamente() 
    elif lance == 1 and computador == 'PEDRA': 
        print('Resultado: EMPATE') 
        jogar_novamente() 
    elif lance == 1 and computador == 'TESOURA': 
        print('Resultado: VOCÊ VENCEU')   
        meu_placar += 1 
        jogar_novamente() 
    elif lance == 2 and computador == 'PAPEL': 
        print('Resultado: VOCÊ VENCEU') 
        meu_placar += 1 
        jogar_novamente() 
    elif lance == 2 and computador == 'PEDRA': 
        print('Resultado: VOCÊ PERDEU') 
        placar_computador += 1 
        jogar_novamente() 
    elif lance == 2 and computador == 'TESOURA': 
        print('Resultado: EMPATE') 
        jogar_novamente() 

def jogar_novamente(): #chama menu de opções para jogar novamente

    print('')
    print('Jogar novamente? 0 - SIM | 1 - NÃO') #menu ficar ou sair do jogo
    quer_voltar = int(input()) #recebe resposta do menu
    if quer_voltar == 0: #se a resposta for 0  
        os.system('cls') #limpa a tela
        inicio_jogo() #chama a função inicio de jogo
    elif quer_voltar == 1: #se a resposta for 1 o jogo sera finalizado
        print('Fim de jogo!')# mostra mensagem de jogo finalizado
    else: #se o usuário digitar uma respota inválida
        os.system('cls') 
        print('opcao invalida! Digite 0 ou 1') #mostra instrução sobre opção válida
        jogar_novamente() #chama a função novamente

inicio_jogo() #inicia o jogo
