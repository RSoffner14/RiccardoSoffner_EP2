from random import randint

spock= int(1)
lagarto= int(2)
pedra= int(3)
papel= int(4)
tesoura= int(5)

jogador_contagem=0
computador_contagem=0

jogador=0
computador=0

while computador_contagem<3 and jogador_contagem<3:
    computador= randint(1,5)
    jogador= int(input("Vamos jogar! Para isso, é necessário que você escolha algum número. 1: spock 2: lagarto, 3: pedra, 4: papel e 5: tesoura:"))
#jogador sendo spock
    if jogador==1:
        if computador==1:
            print("Houve um empate!")
        elif computador==2:
            print("Você perdeu")
            computador_contagem=computador_contagem+1
        elif computador==3:
            print("Voce ganhou")
            jogador_contagem=jogador_contagem+1
        elif computador==4:
            print("Voce perdeu")
            computador_contagem=computador_contagem+1
        elif computador==5:
            print("voce ganhou")
            jogador_contagem=jogador_contagem+1
#jogador sendo lagarto
    if jogador==2:
        print(computador)
        if computador==2:
            print("Houve um empate")
        elif computador==1:
            print("Voce ganhou")
            jogador_contagem=jogador_contagem+1
        elif computador==3:
            print("Voce perdeu")
            computador_contagem=computador_contagem+1
        elif computador==4:
            print("Voce perdeu")
            computador_contagem=computador_contagem+1
        elif computador==5:
            print("voce ganhou")
            jogador_contagem=jogador_contagem+1
#jogador sendo pedra            
    if jogador==3:
        if computador==3:
            print("Houve um empate")
        elif computador==1:
            print("Voce perdeu")
            computador_contagem=computador_contagem+1
        elif computador==2:
            print("Voce ganhou")
            jogador_contagem=jogador_contagem+1
        elif computador==4:
            print("Voce perdeu")
            computador_contagem=computador_contagem+1
        elif computador==5:
            print("voce ganhou")
            jogador_contagem=jogador_contagem+1
            
#jogador sendo papel            
    if jogador==4:
        if computador==4:
            print("Houve um empate")
        elif computador==1:
            print("Voce ganhou")
            jogador_contagem=jogador_contagem+1
        elif computador==2:
            print("Voce perdeu")
            computador_contagem=computador_contagem+1
        elif computador==3:
            print("Voce ganhou")
            jogador_contagem=jogador_contagem+1
        elif computador==5:
            print("voce perdeu")
            computador_contagem=computador_contagem+1

#jogador sendo tesoura    
    if jogador==5:
        if computador==5:
            print("Houve um empate")
        elif computador==1:
            print("Voce perdeu")
            computador_contagem=computador_contagem+1
        elif computador==2:
            print("Voce ganhou")
            jogador_contagem=jogador_contagem+1
        elif computador==3:
            print("Voce perdeu")
            computador_contagem=computador_contagem+1  
        elif computador==4:
            print("voce ganhou")
            jogador_contagem=jogador_contagem+1
            computador_contagem=0
if jogador_contagem==(3):
    print("voce ganhou o jogo, parabéns mestre")
elif computador_contagem==3:
    print("infelizmente voce perdeu o jogo, e uma pena. Tente novamente")
else:
    print("deu erro")