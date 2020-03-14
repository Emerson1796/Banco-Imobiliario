import random
import numpy as np

#1 = O jogador impulsivo ---> O jogador impulsivo compra qualquer propriedade sobre a qual ele parar.
#2 = O jogador exigente ---> O jogador exigente compra qualquer propriedade, desde que o valor do aluguel dela seja maior do que 50.
#3 = O jogador cauteloso ---> O jogador cauteloso compra qualquer propriedade desde que ele tenha uma reserva de 80 saldo sobrando depois de realizada a compra.
#4 = O jogador aleatório ---> O jogador aleatório compra a propriedade que ele parar em cima com probabilidade de 50%.

def game():
    #partidas jogadas
    jogos = 0

    #controle de rodadas
    x = []
    
    #vitorias
    vitórias = []
    rod_jogadas = []
    
    while jogos < 300:
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
        
        while faliu <= 2 and rodadas <= 999:
            comp = 0
            comp_ind = 1
            while comp <= len(ordem)-1:
                if jogadores[comp_ind]['saldo'] >= 1:
                    dado = random.randint(1,6)
                    if (jogadores[ordem[comp]]['pos_jog'] + dado) >= 21:
                        jogadores[ordem[comp]]['pos_jog'] = (jogadores[ordem[comp]]['pos_jog'] + dado) - 21
                        jogadores[ordem[comp]]['saldo'] = jogadores[ordem[comp]]['saldo'] + 100
                    else:
                        jogadores[ordem[comp]]['pos_jog'] = jogadores[ordem[comp]]['pos_jog'] + dado
                    if jogadores[ordem[comp]]['ID'] == propriedades[jogadores[ordem[comp]]['pos_jog']]['dono']:
                        jogadores[ordem[comp]]['saldo']
                    elif propriedades[jogadores[ordem[comp]]['pos_jog']]['dono'] == 'null' and propriedades[jogadores[ordem[comp]]['pos_jog']]['valor'] < jogadores[ordem[comp]]['saldo']:
                        if ordem[comp] == 1:
                            jogadores[ordem[comp]]['saldo'] = jogadores[ordem[comp]]['saldo'] - propriedades[jogadores[ordem[comp]]['pos_jog']]['valor']
                            propriedades[jogadores[ordem[comp]]['pos_jog']]['dono'] = 1
                        elif ordem[comp] == 2:
                            if propriedades[jogadores[ordem[comp]]['pos_jog']]['aluguel'] >= 50:
                                jogadores[ordem[comp]]['saldo'] = jogadores[ordem[comp]]['saldo'] - propriedades[jogadores[ordem[comp]]['pos_jog']]['valor']
                                propriedades[jogadores[ordem[comp]]['pos_jog']]['dono'] = 2
                            else:
                                 jogadores[ordem[comp]]['saldo']
                        elif ordem[comp] == 3:
                            saldo_ver_3 = jogadores[ordem[comp]]['saldo'] * 0.20
                            if propriedades[jogadores[ordem[comp]]['pos_jog']]['valor'] <= saldo_ver_3:
                                jogadores[ordem[comp]]['saldo'] = jogadores[ordem[comp]]['saldo'] - propriedades[jogadores[ordem[comp]]['pos_jog']]['valor']
                                propriedades[jogadores[ordem[comp]]['pos_jog']]['dono'] = 3
                            else:
                                 jogadores[ordem[comp]]['saldo']
                        elif ordem[comp] == 4:
                            saldo_ver_4 = random.randint(0,1)
                            if  saldo_ver_4 == 1:
                                jogadores[ordem[comp]]['saldo'] = jogadores[ordem[comp]]['saldo'] - propriedades[jogadores[ordem[comp]]['pos_jog']]['valor']
                                propriedades[jogadores[ordem[comp]]['pos_jog']]['dono'] = 4
                    elif propriedades[jogadores[ordem[comp]]['pos_jog']]['dono'] == 'iniciar':
                        jogadores[ordem[comp]]['saldo']
                    elif propriedades[jogadores[ordem[comp]]['pos_jog']]['dono'] == 'null'and propriedades[jogadores[ordem[comp]]['pos_jog']]['valor'] >= jogadores[ordem[comp]]['saldo']:
                        jogadores[ordem[comp]]['saldo']
                    else:
                        jogadores[ordem[comp]]['saldo'] = jogadores[ordem[comp]]['saldo'] - propriedades[jogadores[ordem[comp]]['pos_jog']]['aluguel']
                        jogadores[ propriedades[jogadores[ordem[comp]]['pos_jog']]['dono']]['saldo'] = propriedades[jogadores[ordem[comp]]['pos_jog']]['aluguel']+ jogadores[ propriedades[jogadores[ordem[comp]]['pos_jog']]['dono']]['saldo']
                else:
                    jogadores[ordem[comp]]['status'] = 'faliu'
                    controle = 0
                    faliu += 1
                    while controle <=20:
                        if jogadores[ordem[comp]]['ID'] == propriedades[controle]['dono']:
                            propriedades[controle]['dono'] = 'null'
                        controle += 1
                    del(ordem[comp])
                comp += 1
                comp_ind += 1
            rodadas += 1
            
        comp_final = 0
        saldo_fim = []
        while comp_final <= len(ordem)-1:
            saldo_fim.append(jogadores[ordem[comp_final]]['saldo'])
            comp_final += 1

        vitórias.append(ordem[saldo_fim.index(max(saldo_fim))])
        
        v0 = vitórias.count(1)/len(vitórias)
        v1 = vitórias.count(2)/len(vitórias)
        v2 = vitórias.count(3)/len(vitórias)
        v3 = vitórias.count(4)/len(vitórias)

        if v0 > v1 and v0 > v2 and v0 > v3:
            melhor_jogador = "Impulsivo"
        elif v1 > v0 and v1 > v2 and v1 > v3:
            melhor_jogador = "Exigente"
        elif v2 > v0 and v2 > v1 and v2 > v3:    
            melhor_jogador = "Cauteloso"
        elif v3 > v0 and v3 > v1 and v3 > v2:    
            melhor_jogador = "Aleatório"
        
        x.append(rodadas)
        time_out = x.count(1000)
        med_rod = np.mean(x)
        jogos += 1
        
    print("\nMédia de Rodadas: " + str("%.2f" % (med_rod)))
    print("Nº de Time Out: " + str(time_out))
    print("vitórias Perfil Impulsivo: " + str("%.2f" % (v0*100))+"%")
    print("vitórias Perfil Exigente: " + str("%.2f" % (v1*100))+"%")
    print("vitórias Perfil Cauteloso: " + str("%.2f" % (v2*100))+"%")
    print("vitórias Perfil Aleatório: " + str("%.2f" % (v3*100))+"%")
    print("Melhor jogador é: " + melhor_jogador + "\n\n")
                            
opcao = 0;
while opcao != "2":
    opcao = input("Digite 1 para iniciar jogo\nDigite 2 para fechar programa\n")
    if opcao == "1":
        game()

