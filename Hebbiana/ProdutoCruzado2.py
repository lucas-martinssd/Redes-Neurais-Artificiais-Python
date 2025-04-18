#ProdutoCruzado2

W = [
    [10, 2, 2, 6],
    [2, 10, 2, -2],
    [2, 2, 10, -2],
    [6, -2, -2, 10]
]

O = [[0 for _ in range(10)] for _ in range(4)]

X = [
    [1, -1, -1, 1, -1, 1, 1, -1, -1, 1],
    [1, -1, -1, -1, 1, -1, 1, -1, 1, 1],
    [1, 1, -1, -1, -1, 1, 1, -1, 1, -1],
    [-1, -1, -1, 1, -1, 1, 1, 1, -1, 1]
]

for i in range(4):
    for k in range(10):
        for j in range(4):
            O[i][k]=O[i][k]+W[i][j]*X[j][k]
            
for i in range(4):
    for k in range(10):
        print(f"{O[i][j]:8.4f}", end = " ")
    print()