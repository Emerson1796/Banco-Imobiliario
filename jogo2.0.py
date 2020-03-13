import random
import numpy as np

#1 = O jogador impulsivo ---> O jogador impulsivo compra qualquer propriedade sobre a qual ele parar.
#2 = O jogador exigente ---> O jogador exigente compra qualquer propriedade, desde que o valor do aluguel dela seja maior do que 50.
#3 = O jogador cauteloso ---> O jogador cauteloso compra qualquer propriedade desde que ele tenha uma reserva de 80 saldo sobrando depois de realizada a compra.
#4 = O jogador aleatório ---> O jogador aleatório compra a propriedade que ele parar em cima com probabilidade de 50%.

def game():
    #partidas jogadas
    jogos = 0

    #vitorias
    vitórias = []
    
    while jogos < 1:
        #propriedades e alugueis
        propriedades = dict()
        propriedades[0] = {'posição' : 0, 'nome': 'Inicio', 'valor': 0, 'aluguel': 0, 'dono': "iniciar"}
        propriedades[1] = {'posição' : 1, 'nome': 'Jardim Botânico', 'valor': 50, 'aluguel': 12, 'dono': "null"}
        propriedades[2] = {'posição' : 2, 'nome':  'Praça da Sé', 'valor': 50, 'aluguel': 4, 'dono': "null"}
        propriedades[3] = {'posição' : 3, 'nome':  'Av. do Contorno', 'valor': 100, 'aluguel': 24, 'dono': "null"}
        propriedades[4] = {'posição' : 4, 'nome':  'Av. Recife', 'valor': 50, 'aluguel': 8, 'dono': "null"}
        propriedades[5] = {'posição' : 5, 'nome':  'Av. Niemeyer', 'valor': 100, 'aluguel': 32, 'dono': "null"}
        propriedades[6] = {'posição' : 6, 'nome':  'Praça dos Três Poderes', 'valor': 200, 'aluguel': 56, 'dono': "null"}
        propriedades[7] = {'posição' : 7, 'nome':  'Barra da Tijuca', 'valor': 150, 'aluguel': 52, 'dono': "null"}
        propriedades[8] = {'posição' : 8, 'nome':  'Av. Ipiranga', 'valor': 100, 'aluguel': 20, 'dono': "null"}
        propriedades[9] = {'posição' : 9, 'nome':  'Av. Paulista', 'valor': 200, 'aluguel': 52, 'dono': "null"}
        propriedades[10] = {'posição' : 10, 'nome':  'Ponte Rio-Niterói', 'valor': 150, 'aluguel': 44, 'dono': "null"}
        propriedades[11] = {'posição' : 11, 'nome':  'Marina da Glória', 'valor': 150, 'aluguel': 44, 'dono': "null"}
        propriedades[12] = {'posição' : 12, 'nome':  'Av. Ibirapuera', 'valor': 200, 'aluguel': 52, 'dono': "null"}
        propriedades[13] = {'posição' : 13, 'nome':  'Av. Beira Mar', 'valor': 50, 'aluguel': 12, 'dono': "null"}
        propriedades[14] = {'posição' : 14, 'nome':  'Ponte Guaíba', 'valor': 100, 'aluguel': 20, 'dono': "null"}
        propriedades[15] = {'posição' : 15, 'nome':  'Praça Castro Alves', 'valor': 50, 'aluguel': 16, 'dono': "null"}
        propriedades[16] = {'posição' : 16, 'nome':  'Av. Juscelino Kubitschek', 'valor': 150, 'aluguel': 36, 'dono': "null"}
        propriedades[17] = {'posição' : 17, 'nome':  'Av. São João', 'valor': 150, 'aluguel': 40, 'dono': "null"}
        propriedades[18] = {'posição' : 18, 'nome':  'Rua Oscar Freire', 'valor': 150, 'aluguel': 52, 'dono': "null"}
        propriedades[19] = {'posição' : 19, 'nome':  'Higienópolis', 'valor': 200, 'aluguel': 70, 'dono': "null"}
        propriedades[20] = {'posição' : 20, 'nome':  'Jardins', 'valor': 200, 'aluguel': 100, 'dono': "null"}

        #jogadores
        jogadores = dict()
        jogadores[1] = {'ID': 1 ,'jogador':'impulsivo', 'saldo': 300, 'pos_jog': 0, 'status':'ok'}
        jogadores[2] = {'ID': 2 ,'jogador':'exigente', 'saldo': 300, 'pos_jog': 0, 'status':'ok'}
        jogadores[3] = {'ID': 3 ,'jogador':'cauteloso', 'saldo': 300, 'pos_jog': 0, 'status':'ok'}
        jogadores[4] = {'ID': 4 ,'jogador':'aleatório', 'saldo': 300, 'pos_jog': 0, 'status':'ok'}

        #controle de falência
        faliu = 0
        z = 1

        #ordem
        ordem =[]
        cont = 0

        while True:
            num = random.randint(1,4)
            if num not in ordem:
                ordem.append(num)
                cont +=1
            if cont >=4:
                break

        #rodadas
        rodadas = 1
        
        while z <= 4:
            if jogadores[z]['status'] == 'faliu':
                if faliu >= 4:
                    faliu
                else:
                    faliu += 1
                print(faliu)
            z += 1
        while faliu < 3 and rodadas <= 5:
            comp = 0
            comp_ind = 1
            while comp <= len(ordem)-1:
                if jogadores[comp_ind]['saldo'] > 0:
                    dado = random.randint(1,6)
                    if (jogadores[ordem[comp]]['pos_jog'] + dado) >= 21:
                        jogadores[ordem[comp]]['pos_jog'] = (jogadores[ordem[comp]]['pos_jog'] + dado) - 21
                        jogadores[ordem[comp]]['saldo'] = jogadores[ordem[comp]]['saldo'] + 100
                    else:
                        jogadores[ordem[comp]]['pos_jog'] = jogadores[ordem[comp]]['pos_jog'] + dado
                    if ordem[comp] == propriedades[jogadores[ordem[comp]]['pos_jog']]['dono']:
                        jogadores[ordem[comp]]['saldo']
                        print(jogadores[ordem[comp]]['pos_jog'])
                    elif propriedades[jogadores[ordem[comp]]['pos_jog']]['dono'] == 'null':
                        if ordem[comp] == 1:
                            
                        elif ordem[comp] == 2:
                            
                        elif ordem[comp] == 3:
                            
                        elif ordem[comp] == 4:
                            
                    elif propriedades[jogadores[ordem[comp]]['pos_jog']]['dono'] == 'iniciar':
                        jogadores[ordem[comp]]['saldo']
                    else:
                        jogadores[ordem[comp]]['saldo'] = jogadores[ordem[comp]]['saldo'] - propriedades[jogadores[ordem[comp]]['pos_jog']]['aluguel']
                        jogadores[ propriedades[jogadores[ordem[comp]]['pos_jog']]['dono']]['saldo'] = propriedades[jogadores[ordem[comp]]['pos_jog']]['aluguel'] + jogadores[ propriedades[jogadores[ordem[comp]]['pos_jog']]['dono']]['saldo']
                comp += 1
                comp_ind += 1
            rodadas += 1
        jogos += 1
                            
opcao = 0;
while opcao != "2":
    opcao = input("Digite 1 para iniciar jogo\nDigite 2 para fechar programa\n")
    if opcao == "1":
        game()

