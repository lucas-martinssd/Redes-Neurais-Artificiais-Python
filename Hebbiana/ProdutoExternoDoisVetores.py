#ProdutoExternoDoisVetores

I = 4
J = 4

X = [1, 1, 1, -1]

W = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

for i in range(I):
    for j in range(J):
        W[i][j] = X[i]*X[j]
        print(f"{W[i][j]:8.4f}", end=" ")
    print()