ETA = 0.2

X = [
    [-1, 1],
    [-1, -1],
    [1, -1],
    [-1, 1]
]

W = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

O = [[0 for _ in range(2)] for _ in range(4)]

E = [[0 for _ in range(2)] for _ in range(4)]

DELTA = [[0 for _ in range(4)] for _ in range(4)]

def zerandoMatrizes():
    for i in range(4):
        for j in range(2):
            O[i][j]=0
    for i in range(4):
        for j in range(4):
            DELTA[i][j]=0

def resposta():
    print("\nResposta/Erro/DeltaW")
    #Produto Cruzado
    for i in range(4):
        for k in range(2):
            for j in range(4):
                O[i][k]+=W[i][j]*X[j][k]
        
    for i in range(4):
        for k in range(2):
            print(f"{O[i][k]:5.10f}", end = " ")
        print()

def calcularErro():
    print("\nErro: ")
    for i in range(4):
        for k in range(2):
            E[i][k]=X[i][k]-O[i][k]
            print(f"{O[i][k]:5.10f}", end = " ")
        print()

def geraDelta():
    #Calcular a matriz de correção
    print("\nDelta: ")
    for i in range(4):
        for j in range(4):
            for k in range(2):
                DELTA[i][j]+=E[i][k]*X[j][k]
                
    #Multiplica DELTA pela constante
    for i in range(4):
        for j in range(4):
            DELTA[i][j]*=ETA
            print(f"{DELTA[i][j]:5.10f}", end = " ")
        print()

def corrigirW():
    print("\nMatriz de pesos: ")
    for i in range(4):
        for j in range(4):
            W[i][j]+=DELTA[i][j]
            print(f"{W[i][j]:5.10f}", end = " ")
        print()    

for epoca in range(30):
    print(f"\n______ Iteração {epoca + 1} _______")
    zerandoMatrizes()
    resposta()
    calcularErro()
    geraDelta()
    corrigirW()