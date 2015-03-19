# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 19:31:36 2015

@author: Riccardo
"""

from random import randint

jogador1=int(0)
computador1=int(0)
spock= int(1)
tesoura= int(2)
lagarto= int(3)
pedra= int(4)
papel= int(5)

while (jogador1<3) and (computador1<3):
    if jogador1==3:
        print("
        break
    print (jogador1) 
    if computador1==3:
        print("O computador ganhou, tente novamente.")
        break
        print (computador1)       
    computador = randint(1,5)
    jogador=int(input("Escolha uma opção jogador! O numero 1 é o spock, 2 é tesoura, 3 é lagarto, 4 é pedra e 5 é papel:"))      
    
    if computador == jogador:
        print("Houve um empate! Tente novamente")        
        
#computador sendo spock
    elif computador == (1) and jogador == (2):
        print("Você perdeu!")
        computador = computador+1
        jogador = 0
    elif computador == (1) and jogador == (3):
        print("Você venceu!")
        jogador= jogador+1
        computador= 0
    elif computador == (1) and jogador == (4):
        print("Você perdeu!")
        computador=computador+1
        jogador=0
    elif computador == (1) and jogador == (5):
        print("Você venceu!")
        jogador=jogador+1
        computador=0
#computador sendo tesoura        
    elif computador == (2) and (jogador == (1) or jogador == (4)):
        print("Você venceu!")
        jogador=jogador+1
        computador=0
    elif computador ==2 and (jogador == (3) or jogador ==(5)):
        print("Você perdeu!")
        computador=computador+1
        jogador=0
        
#computador sendo lagarto
    elif computador ==(3) and (jogador==(1) or jogador == (5)):
        print("Você perdeu!")
        computador=computador+1
        jogador=0
    elif computador ==(3) and  (jogador == (4) or jogador==(2)):
        print("Você ganhou!")
        jogador=jogador+1
        computador=0
#computador sendo pedra                 
    elif computador ==(4) and (jogador==(2) or jogador==(3)):
        print("Você perdeu!")        
        computador=computador+1
        jogador=0
    elif computador ==(4) and (jogador==(1) or jogador==(5)):
        print("Você ganhou!")        
        jogador=jogador+1
        computador=0
#computador sendo papel        
    elif computador ==(5) and (jogador==(4) or jogador==(1)):
        print("Você perdeu!")
        computador=computador+1
        jogador=0
    elif computador ==(5) and (jogador==(2) or jogador==(3)):
        print("Você ganhou!")
        jogador=jogador+1
        computador=0
         
if jogador1==3:
    print("voce ganhou o jogo, parabens")
else:
    print("voce perdeu o jogo, e uma pena")