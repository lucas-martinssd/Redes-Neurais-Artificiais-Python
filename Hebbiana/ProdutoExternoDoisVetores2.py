#ProdutoExternoDoisVetores2

I = 4
J = 4

def produtoExterno(W, X):
    for i in range(I):
        for j in range(J):
            W[i][j] = X[i]*X[j]
            print(f"{W[i][j]:8.4f}", end = " ")
        print()
        

X=[1, 1, 1, -1]
W=[[0 for _ in range(J)] for _ in range(I)]
produtoExterno(W, X)
