import random
import numpy as np

#0 = O jogador impulsivo ---> O jogador impulsivo compra qualquer propriedade sobre a qual ele parar.
#1 = O jogador exigente ---> O jogador exigente compra qualquer propriedade, desde que o valor do aluguel dela seja maior do que 50.
#2 = O jogador cauteloso ---> O jogador cauteloso compra qualquer propriedade desde que ele tenha uma reserva de 80 saldo sobrando depois de realizada a compra.
#3 = O jogador aleatório ---> O jogador aleatório compra a propriedade que ele parar em cima com probabilidade de 50%.

#partidas jogadas
jogos = 0

#vitorias
vitórias = []

while jogos < 1:
    #propriedades e alugueis
    propriedades = dict()
    propriedades[1] = {'posição' : 1, 'nome': 'Jardim Botânico', 'valor': 50, 'aluguel': 12, 'dono': ""}
    propriedades[2] = {'posição' : 2, 'nome':  'Praça da Sé', 'valor': 50, 'aluguel': 4, 'dono': ""}
    propriedades[3] = {'posição' : 3, 'nome':  'Av. do Contorno', 'valor': 100, 'aluguel': 24, 'dono': ""}
    propriedades[4] = {'posição' : 4, 'nome':  'Av. Recife', 'valor': 50, 'aluguel': 8, 'dono': ""}
    propriedades[5] = {'posição' : 5, 'nome':  'Av. Niemeyer', 'valor': 100, 'aluguel': 32, 'dono': ""}
    propriedades[6] = {'posição' : 6, 'nome':  'Praça dos Três Poderes', 'valor': 200, 'aluguel': 56, 'dono': ""}
    propriedades[7] = {'posição' : 7, 'nome':  'Barra da Tijuca', 'valor': 150, 'aluguel': 52, 'dono': ""}
    propriedades[8] = {'posição' : 8, 'nome':  'Av. Ipiranga', 'valor': 100, 'aluguel': 20, 'dono': ""}
    propriedades[9] = {'posição' : 9, 'nome':  'Av. Paulista', 'valor': 200, 'aluguel': 52, 'dono': ""}
    propriedades[10] = {'posição' : 10, 'nome':  'Ponte Rio-Niterói', 'valor': 150, 'aluguel': 44, 'dono': ""}
    propriedades[11] = {'posição' : 11, 'nome':  'Marina da Glória', 'valor': 150, 'aluguel': 44, 'dono': ""}
    propriedades[12] = {'posição' : 12, 'nome':  'Av. Ibirapuera', 'valor': 200, 'aluguel': 52, 'dono': ""}
    propriedades[13] = {'posição' : 13, 'nome':  'Av. Beira Mar', 'valor': 50, 'aluguel': 12, 'dono': ""}
    propriedades[14] = {'posição' : 14, 'nome':  'Ponte Guaíba', 'valor': 100, 'aluguel': 20, 'dono': ""}
    propriedades[15] = {'posição' : 15, 'nome':  'Praça Castro Alves', 'valor': 50, 'aluguel': 16, 'dono': ""}
    propriedades[16] = {'posição' : 16, 'nome':  'Av. Juscelino Kubitschek', 'valor': 150, 'aluguel': 36, 'dono': ""}
    propriedades[17] = {'posição' : 17, 'nome':  'Av. São João', 'valor': 150, 'aluguel': 40, 'dono': ""}
    propriedades[18] = {'posição' : 18, 'nome':  'Rua Oscar Freire', 'valor': 150, 'aluguel': 52, 'dono': ""}
    propriedades[19] = {'posição' : 19, 'nome':  'Higienópolis', 'valor': 200, 'aluguel': 70, 'dono': ""}
    propriedades[20] = {'posição' : 20, 'nome':  'Jardins', 'valor': 200, 'aluguel': 100, 'dono': ""}

    #jogadores
    jogadores = dict()
    jogadores[1] = {'jogador':'impulsivo', 'saldo': 300, 'pos_jog': 0, 'status':'faliu'}
    jogadores[2] = {'jogador':'exigente', 'saldo': 300, 'pos_jog': 0, 'status':'faliu'}
    jogadores[3] = {'jogador':'cauteloso', 'saldo': 300, 'pos_jog': 0, 'status':'faliu'}
    jogadores[4] = {'jogador':'aleatório', 'saldo': 300, 'pos_jog': 0, 'status':'faliu'}

    #controle de falência
    faliu = 1
    erro = 0

    #ordem
    ordem =[]
    cont = 0

    while True:
        num = random.randint(0,3)
        if num not in ordem:
            ordem.append(num)
            cont +=1
        if cont >=4:
            break

    #rodadas
    rodadas = 1
    
    while erro <= 3:
        if jogadores[faliu]['status'] == 'faliu':
            if faliu >= 4:
                faliu
            else:
                faliu += 1
            print(faliu)
        else:
            print('fim')
        erro += 1
    jogos += 1
