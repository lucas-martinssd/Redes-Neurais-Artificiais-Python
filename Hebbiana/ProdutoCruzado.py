#ProdutoCruzado

W = [[0 for _ in range(4)] for _ in range(4)]
X = [
    [ 1,-1,-1, 1,-1, 1, 1,-1,-1, 1],
    [ 1,-1,-1,-1, 1,-1, 1,-1, 1, 1],
    [ 1, 1,-1,-1,-1, 1, 1,-1, 1,-1],
    [-1,-1,-1, 1,-1, 1, 1, 1,-1, 1] 
]

for i in range(4):
    for j in range(4):
        W[i][j]=0
        for k in range(10):
            W[i][j] = W[i][j]+X[i][k]*X[j][k]
    
for i in range(4):
    for j in range(4):
        print(f"{W[i][j]:8.4f}", end = " ")
    print()
print()