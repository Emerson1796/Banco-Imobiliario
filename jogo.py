import random
import numpy as np


def programa():
    #partidas jogadas
    jogos = 0

    #propriedades e alugueis
    nome_propriedades =["Inicio", "Jardim Botânico", "Av. Niemeyer", "Av. Paulista", "Av. Beira Mar"
                        , "Praça da Sé", "Praça dos Três Poderes", "Ponte Rio-Niterói", "Ponte Guaíba"
                        , "Av. do Contorno", "Barra da Tijuca", "Marina da Glória", "Praça Castro Alves", "Av. São João"
                        , "Av. Recife", "Av. Ipiranga", "Av. Ibirapuera", "Av. Juscelino Kubitschek", "Rua Oscar Freire", "Higienópolis", "Jardins"]
    propriedades = [0, 50, 50, 100, 50, 100, 200, 150, 100, 200, 150, 150, 200, 50, 100, 50, 150, 150, 150, 200, 200]
    aluguel =      [0, 12, 4, 24, 8, 32, 56, 52, 20, 52, 44, 44, 52, 12, 20, 16, 36, 40, 52, 70, 100]

    #0 = O jogador impulsivo ---> O jogador impulsivo compra qualquer propriedade sobre a qual ele parar.
    #1 = O jogador exigente ---> O jogador exigente compra qualquer propriedade, desde que o valor do aluguel dela seja maior do que 50.
    #2 = O jogador cauteloso ---> O jogador cauteloso compra qualquer propriedade desde que ele tenha uma reserva de 80 saldo sobrando depois de realizada a compra.
    #3 = O jogador aleatório ---> O jogador aleatório compra a propriedade que ele parar em cima com probabilidade de 50%.

    #vitorias individuais
    v0 = 0
    v1 = 0
    v2 = 0
    v3 = 0

    #variaveis de controle de rodadas jogadas
    e = 0
    z = []

    while (jogos <= 299):
        
        #ordem de jogo
        ordem = []
        cont = 0
        i = 0
        
        #numero de rodadas
        rodadas = 0

        #propriedas dos jogadores
        pp0 = []
        pp1 = []
        pp2 = []
        pp3 = []


        #saldo geral
        saldo = []
        vitorias = []
        
        #posicao
        pos_impulsivo = 0
        pos_exigente = 0
        pos_cauteloso = 0
        pos_aleatório = 0

        #saldo
        saldo_impulsivo = 300
        saldo_exigente = 300
        saldo_cauteloso = 300
        saldo_aleatório = 300

        jogadores = 0

        faliu =[]
        
        while True:
            num = random.randint(0,3)
            if num not in ordem:
                ordem.append(num)
                cont +=1
            if cont >=4:
                break
        rodadas = 0   
        e = 0
        while(rodadas <= 999) and len(faliu) < 3:
            jogadores = 0
            i=0
            
            e += 1
            while i < 3:
                           
                if ordem[jogadores] == 0:
                    
                    if saldo_impulsivo > 0:
                        dado = random.randint(1,6)
                        if (pos_impulsivo + dado) > 20:
                            pos_impulsivo = (dado +  pos_impulsivo) - 20
                            saldo_impulsivo = saldo_impulsivo + 100
                            
                                
                        else:
                            
                            pos_impulsivo = pos_impulsivo + dado
                            
                        n_pos0 = nome_propriedades[pos_impulsivo]
                       
                        if n_pos0 in pp1:
                                saldo_impulsivo = saldo_impulsivo - aluguel[pos_impulsivo]
                                saldo_exigente = saldo_exigente + aluguel[pos_impulsivo]
                               
                        elif n_pos0 in pp2:
                                saldo_impulsivo = saldo_impulsivo - aluguel[pos_impulsivo]
                                saldo_cauteloso = saldo_cauteloso + aluguel[pos_impulsivo]

                        elif n_pos0 in pp3:
                                saldo_impulsivo = saldo_impulsivo - aluguel[pos_impulsivo]
                                saldo_aleatório = saldo_aleatório + aluguel[pos_impulsivo]
                        elif n_pos0 in pp0:
                                saldo_impulsivo
                        else:
                            if propriedades[pos_impulsivo] > saldo_impulsivo:
                                saldo_impulsivo
                            else:
                                nova0 = nome_propriedades[pos_impulsivo]
                                pp0.append(nova0)
                                saldo_impulsivo = saldo_impulsivo - propriedades[pos_impulsivo]
                    elif saldo_impulsivo <= 0:
                        if 0 not in faliu:
                            faliu.append(0)
                            pp0.clear()
                            break
                        
                elif ordem[jogadores] == 1:
                    
                    if saldo_exigente > 0:
                        dado = random.randint(1,6)
                        if (pos_exigente + dado) >= 21:
                            pos_exigente = (dado +  pos_exigente) - 20
                            saldo_exigente = saldo_exigente + 100
                            pos_exigente = pos_exigente + dado
                                
                        elif pos_cauteloso + dado <= 20:
                            
                            pos_exigente = pos_exigente + dado
                            n_pos1 = nome_propriedades[pos_exigente]

                        if n_pos1 in pp0:
                                saldo_exigente = saldo_exigente - aluguel[pos_exigente]
                                saldo_impulsivo = saldo_impulsivo + aluguel[pos_exigente]
                               
                        elif n_pos1 in pp2:
                                saldo_exigente = saldo_exigente - aluguel[pos_exigente]
                                saldo_cauteloso = saldo_cauteloso + aluguel[pos_exigente]

                        elif n_pos1 in pp3:
                                saldo_exigente = saldo_exigente - aluguel[pos_exigente]
                                saldo_aleatório = saldo_aleatório + aluguel[pos_exigente]
                        elif n_pos1 in pp1:
                                saldo_exigente
                        else:
                            if aluguel[pos_exigente] > 50 and propriedades[pos_exigente] < saldo_exigente:
                                nova1 = nome_propriedades[pos_exigente]
                                pp1.append(nova1)
                                saldo_exigente = saldo_exigente - propriedades[pos_exigente]
                                
                            else:
                                saldo_exigente
                    else:
                        if 1 not in faliu:
                            faliu.append(1)
                            pp1.clear()
                            break
                        
                elif ordem[jogadores] == 2:
                    
                    if saldo_cauteloso > 0:
                        dado = random.randint(1,6)
                        if (pos_cauteloso + dado) >= 21:
                            pos_cauteloso = (dado +  pos_cauteloso) - 20
                            saldo_cauteloso = saldo_cauteloso + 100
                                
                        elif pos_cauteloso + dado <= 20:
                            
                            pos_cauteloso = pos_cauteloso + dado
                            
                        n_pos2 = nome_propriedades[pos_cauteloso]

                        if n_pos2 in pp0:
                                saldo_cauteloso = saldo_cauteloso - aluguel[pos_cauteloso]
                                saldo_impulsivo = saldo_impulsivo + aluguel[pos_cauteloso]
                               
                        elif n_pos2 in pp1:
                                saldo_cauteloso = saldo_cauteloso - aluguel[pos_cauteloso]
                                saldo_exigente = saldo_exigente + aluguel[pos_cauteloso]

                        elif n_pos2 in pp3:
                                saldo_cauteloso = saldo_cauteloso - aluguel[pos_cauteloso]
                                saldo_aleatório = saldo_aleatório + aluguel[pos_cauteloso]
                        elif n_pos2 in pp2:
                                saldo_cauteloso
                        
                        else:
                            compra2 = saldo_cauteloso * 0.2
                            if compra2 >= propriedades[pos_cauteloso]:
                                nova2 = nome_propriedades[pos_cauteloso]
                                pp2.append(nova2)
                                saldo_cauteloso = saldo_cauteloso - propriedades[pos_cauteloso]
                            else:
                                saldo_cauteloso
                    else:
                        if 2 not in faliu:
                            faliu.append(2)
                            pp2.clear()
                            break
                        
                elif ordem[jogadores]== 3:
                    
                    if saldo_aleatório > 0:
                        dado = random.randint(1,6)
                        if (pos_aleatório + dado) >= 21:
                            pos_aleatório = (dado +  pos_aleatório) - 20
                            saldo_aleatório = saldo_aleatório + 100
                                
                        elif pos_aleatório + dado <= 20:
                            
                            pos_aleatório = pos_aleatório + dado
                            
                        n_pos3 = nome_propriedades[pos_aleatório]

                        if n_pos3 in pp0:
                                saldo_aleatório = saldo_aleatório - aluguel[pos_aleatório]
                                saldo_impulsivo = saldo_impulsivo + aluguel[pos_aleatório]
                               
                        elif n_pos3 in pp1:
                                saldo_aleatório = saldo_aleatório - aluguel[pos_aleatório]
                                saldo_exigente = saldo_exigente + aluguel[pos_aleatório]

                        elif n_pos3 in pp2:
                                saldo_aleatório = saldo_aleatório - aluguel[pos_aleatório]
                                saldo_cauteloso = saldo_cauteloso + aluguel[pos_aleatório]
                        elif n_pos3 in pp3:
                                saldo_aleatório
                        
                        else:
                            compra3 = random.randint(0,1)
                            if compra3 == 1 and propriedades[pos_aleatório] < saldo_aleatório:
                                nova3 = nome_propriedades[pos_aleatório]
                                pp3.append(nova3)
                                saldo_aleatório = saldo_aleatório - propriedades[pos_aleatório]
                            else:
                                saldo_aleatório
                                
                    else:
                        if 3 not in faliu:
                            faliu.append(3)
                            pp3.clear()
                            break
                
                jogadores += 1

                i += 1
                
            rodadas += 1

        k = 0
        while k <= 3:
            if ordem[k] == 0:
                saldo.append(saldo_impulsivo)
            elif ordem[k] == 1:
                saldo.append(saldo_exigente)
            elif ordem[k] == 2:
                saldo.append(saldo_cauteloso)
            elif ordem[k] == 3:
                saldo.append(saldo_aleatório)
            
            k +=1
            n_max = max(saldo)
            n_pos = saldo.index(n_max)
            
            if ordem[n_pos] == 0:
                vitorias.append(0)
            elif ordem[n_pos] == 1:
                vitorias.append(1)
            elif ordem[n_pos] == 2:
                vitorias.append(2)
            elif ordem[n_pos] == 3:
                vitorias.append(3)
            
            v0 = vitorias.count(0)/len(vitorias)
            v1 = vitorias.count(1)/len(vitorias)
            v2 = vitorias.count(2)/len(vitorias)
            v3 = vitorias.count(3)/len(vitorias)

            if v0 > v1 and v0 > v2 and v0 > v3:
                melhor_jogador = "Impulsivo"
            elif v1 > v0 and v1 > v2 and v1 > v3:
                melhor_jogador = "Exigente"
            elif v2 > v0 and v2 > v1 and v2 > v3:    
                melhor_jogador = "Cauteloso"
            elif v3 > v0 and v3 > v1 and v3 > v2:    
                melhor_jogador = "Aleatório"
                    
        z.append(e)    
        jogos +=1
        num_rod = []
        med_rod = np.mean(z)
        time_out = z.count(1000)

        
        
        

    print("\nMédia de Rodadas: " + str(med_rod))
    print("Nº de Time Out: " + str(time_out))
    print("vitórias Perfil Impulsivo: " + str(v0*100)+"%")
    print("vitórias Perfil Exigente: " + str(v1*100)+"%")
    print("vitórias Perfil Cauteloso: " + str(v2*100)+"%")
    print("vitórias Perfil Aleatório: " + str(v3*100)+"%")
    print("Melhor jogador é: " + melhor_jogador + "\n\n")

opcao = 0;
while opcao != "2":
    opcao = input("Digite 1 para iniciar jogo\nDigite 2 para fechar programa\n")
    if opcao == "1":
        programa()
