from pymongo import MongoClient
cliente = MongoClient('192.X.X.X', 27020) #Aqui o ip deve ser o de vcs.
banco = cliente.artigo_xadrez

partidas = []
i = 0
cont = 0
arq = open('lichess_edu_baranowski_2020-04-25.pgn', 'r')
partida = []
for linha in arq:
    
    linha = linha.split('\n')    
    if linha == ['', '']:
        cont+=1
    partida.append(linha)
    
    if cont == 3:
        partidas.append(partida)        
        cont = 0
        partida = []
               
        
for i in range(len(partidas)):
    lista = partidas[i]
    for j in range(len(lista)):
        lista[j].pop()



for i in range(len(partidas)):
    partidas[i].pop()
    partidas[i].pop()
    if len(partidas[i]) == 17:        
        del(partidas[i][15])    
    elif len(partidas[i]) == 19:
        del(partidas[i][17])
    elif len(partidas[i]) == 20:
        del(partidas[i][18])  
    

for i in range(len(partidas)):       
    if (len(partidas[i])) == 18:        
        partida = {
                  "evento": partidas[i][0][0].replace('[', '').replace(']',''),
                  "site": partidas[i][1][0].replace('[', '').replace(']',''),
                  "data": partidas[i][2][0].replace('[', '').replace(']',''),
                  "round": partidas[i][3][0].replace('[', '').replace(']',''),
                  "white": partidas[i][4][0].replace('[', '').replace(']',''),
                  "black": partidas[i][5][0].replace('[', '').replace(']',''),
                  "result": partidas[i][6][0].replace('[', '').replace(']',''),
                  "utcdate": partidas[i][7][0].replace('[', '').replace(']',''),
                  "utctime": partidas[i][8][0].replace('[', '').replace(']',''),
                  "whiteelo": partidas[i][9][0].replace('[', '').replace(']',''),
                  "blackelo": partidas[i][10][0].replace('[', '').replace(']',''),
                  "whiteratingdiff": partidas[i][11][0].replace('[', '').replace(']',''),
                  "blackratingdiff": partidas[i][12][0].replace('[', '').replace(']',''),
                  "variant": partidas[i][13][0].replace('[', '').replace(']',''),
                  "timecontrol": partidas[i][14][0].replace('[', '').replace(']',''),
                  "eco": partidas[i][15][0].replace('[', '').replace(']',''),
                  "termination": partidas[i][16][0].replace('[', '').replace(']',''),
                  "notacao": partidas[i][17][0].replace('[', '').replace(']','')
                 }
        pgns = banco.pgns
        partida_id = pgns.insert_one(partida).inserted_id
        #print(partida_id)
        
    elif (len(partidas[i])) == 16:        
        partida = {
                  "evento": partidas[i][0][0].replace('[', '').replace(']',''),
                  "site": partidas[i][1][0].replace('[', '').replace(']',''),
                  "data": partidas[i][2][0].replace('[', '').replace(']',''),
                  "round": partidas[i][3][0].replace('[', '').replace(']',''),
                  "white": partidas[i][4][0].replace('[', '').replace(']',''),
                  "black": partidas[i][5][0].replace('[', '').replace(']',''),
                  "result": partidas[i][6][0].replace('[', '').replace(']',''),
                  "utcdate": partidas[i][7][0].replace('[', '').replace(']',''),
                  "utctime": partidas[i][8][0].replace('[', '').replace(']',''),
                  "whiteelo": partidas[i][9][0].replace('[', '').replace(']',''),
                  "blackelo": partidas[i][10][0].replace('[', '').replace(']',''),
                  "variant": partidas[i][11][0].replace('[', '').replace(']',''),
                  "timecontrol": partidas[i][12][0].replace('[', '').replace(']',''),
                  "eco": partidas[i][13][0].replace('[', '').replace(']',''),
                  "termination": partidas[i][14][0].replace('[', '').replace(']',''),
                  "notacao": partidas[i][15][0].replace('[', '').replace(']','')
                 }
        pgns = banco.pgns
        partida_id = pgns.insert_one(partida).inserted_id

    elif (len(partidas[i])) == 19:        
        partida = {
                  "evento": partidas[i][0][0].replace('[', '').replace(']',''),
                  "site": partidas[i][1][0].replace('[', '').replace(']',''),
                  "data": partidas[i][2][0].replace('[', '').replace(']',''),
                  "round": partidas[i][3][0].replace('[', '').replace(']',''),
                  "white": partidas[i][4][0].replace('[', '').replace(']',''),
                  "black": partidas[i][5][0].replace('[', '').replace(']',''),
                  "result": partidas[i][6][0].replace('[', '').replace(']',''),
                  "utcdate": partidas[i][7][0].replace('[', '').replace(']',''),
                  "utctime": partidas[i][8][0].replace('[', '').replace(']',''),
                  "whiteelo": partidas[i][9][0].replace('[', '').replace(']',''),
                  "blackelo": partidas[i][10][0].replace('[', '').replace(']',''),
                  "whiteratingdiff": partidas[i][11][0].replace('[', '').replace(']',''),
                  "blackratingdiff": partidas[i][12][0].replace('[', '').replace(']',''),                  
                  "title": partidas[i][13][0].replace('[', '').replace(']',''),
                  "variant": partidas[i][14][0].replace('[', '').replace(']',''),
                  "timecontrol": partidas[i][15][0].replace('[', '').replace(']',''),
                  "eco": partidas[i][16][0].replace('[', '').replace(']',''),
                  "termination": partidas[i][17][0].replace('[', '').replace(']',''),
                  "notacao": partidas[i][18][0].replace('[', '').replace(']','')
                 }
        pgns = banco.pgns
        partida_id = pgns.insert_one(partida).inserted_id        


