#3Disciplina: Introdução a programação em python
#Academica: Jéssica Cristina Tironi
#Data: 19/04
def criarMat(e): #funcao que gera o campo minado
    if (e == 1):
        # Campo inicial com minas e dicas
        campo = [["@", "1", "-", "1", "1", "2", "@", "2", "@"],
                ["1", "1", "-", "1", "@", "2", "1", "2", "1"],
                ["-", "-", "-", "1", "1", "1", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
                ["-", "1", "1", "1", "-", "-", "-", "-", "-"],
                ["-", "2", "@", "2", "-", "-", "1", "2", "2"],
                ["-", "2", "@", "2", "-", "-", "1", "@", "@"],
                ["-", "1", "1", "1", "-", "-", "1", "3", "3"],
                ["-", "-", "1", "1", "1", "-", "-", "1", "@"],
                ["-", "-", "1", "@", "1", "-", "-", "1", "1"]]
                  
    if (e == 0):
        # Campo inicial vazio
        campo = [["#", "#", "#", "#", "#", "#", "#", "#", "#"],
                ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
                ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
                ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
                ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
                ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
                ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
                ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
                ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
                ["#", "#", "#", "#", "#", "#", "#", "#", "#"]]

    return campo

def mostrar(campo): #Função mostra campo
    print("\n\n      1   2   3   4   5   6   7   8   9 ")  
    for i in range(0, 10):
        if i == 9:
            print(" {} |".format(i+1), end="")  
        else:
            print("  {} |".format(i+1), end="")  
        for j in range(0, 9):
            print(" {} |".format(campo[i][j]), end="")
        print("")

def Vazios(campo, aux): #Função que verifica se tem mais vazios
        for i in range(0, 10):
            for j in range(0, 9):
                if(campo[i][j] == "-"):
                    try:
                        if(campo[i-1][j-1] == '-'):
                            aux[i-1][j-1] = campo[i-1][j-1]
                    except:
                        i=i

                    try:
                        if(campo[i-1][j] == '-'):
                            aux[i-1][j] =campo[i-1][j]
                    except:
                        i=i
                    
                    try:
                        if(campo[i-1][j+1] == '-'):
                           aux[i-1][j+1] = campo[i-1][j+1]
                    except:
                        i=i
                    
                    try:
                        if(aux[i][j-1] == '-'):
                            aux[i][j-1] = campo[i][j-1]
                    except:
                        i=i
                    
                    try:
                        if(campo[i][j+1] == '-'):
                            aux[i][j+1] = campo[i][j+1]
                    except:
                        i=i
                    
                    try:
                        if(campo[i+1][j-1] == '-'):
                            aux[i+1][j-1] = campo[i+1][j-1]
                    except:
                        i=i
                    
                    try:
                        if(campo[i+1][j] == '-'):
                            aux[i+1][j] = campo[i+1][j]
                    except:
                        i=i
                    
                    try:
                        if(campo[i+1][j+1] == '-'):
                            aux[i+1][j+1] = campo[i+1][j+1]
                    except: 
                        i=i
                                
def jogar(): # Função principal do jogo

    inicio = 0
    while(inicio == 0):
        print("\t\t Bem vindo ao jogo. Boa sorte.")
        fim = 0
        e = 1
        campo = criarMat(e) # Cria o campo com minas
        e = 0
        aux = criarMat(e) # Cria o campo vazio
        tentativas = 41  # Número de tentativas permitidas
        
        mostrar(aux) # Mostra o campo vazio
        
        
        while(fim == 0):
            print("\t Digite as coordenadas      ")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            
            while(linha < 1 or linha > 10 or coluna < 1 or coluna > 9):
                if(linha < 1 or linha > 10 or coluna < 1 or coluna > 9):
                    print("Coordenadas invalidas. Digite novamente.")
                    linha = int(input("Linha: "))
                    coluna = int(input("Coluna: "))
            
            linha = linha - 1 
            coluna = coluna - 1
            
            while(aux[linha][coluna] != '#'):
                if(aux[linha][coluna] != '#'):
                    print("Coordenadas já foram escolhidas. Digite novamente.")
                    linha = int(input("Linha: "))
                    coluna = int(input("Coluna: "))
            
                    linha = linha - 1 
                    coluna = coluna - 1
            
            
            tentativas = tentativas - 1
            if(campo[linha][coluna] == '@'):
                aux[linha][coluna] = campo[linha][coluna]
                mostrar(aux)
                print("\tBUMMM. Você perdeu.")
                fim = 1
            elif(campo[linha][coluna] == '-'):
                Vazios(campo, aux)  # Verifica e revela espaços vazios adjacentes                  
                mostrar(aux)
            else:
                aux[linha][coluna] = campo[linha][coluna]
                mostrar(aux)
            
            if tentativas == 0:
                print("\tParabéns, você venceu")
                fim = 1

        inicio = int(input("Você deseja jogar novamente? (1. Sim 2. Não): "))
        while(inicio < 1 or inicio > 2):
            print("Opção invalida. Digite novamente")
            inicio = int(input("Você deseja jogar novamente? (1. Sim 2. Não): "))
            
        inicio = inicio - 1
                
                      
jogar()
