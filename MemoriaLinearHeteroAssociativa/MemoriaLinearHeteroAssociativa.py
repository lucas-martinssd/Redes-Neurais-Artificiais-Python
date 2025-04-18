X = [
    [ 1, -1, -1,  1, -1],
    [ 1, -1, -1, -1,  1],
    [ 1,  1, -1, -1, -1],
    [-1, -1, -1,  1, -1]
]

T = [
    [ 1, -1, -1,  1, -1],
    [ 1,  1, -1, -1,  1],
    [-1, -1,  1,  1,  1]
]

W = [[0 for _ in range(3)] for _ in range(4)]

for i in range(4):
    for j in range(3):
        soma = 0
        for k in range(5):
            soma += X[i][k] * T[j][k]
        W[i][j] = soma

print("Matriz de Pesos W (4x3):")
for linha in W:
    print(linha)

def lembrar(x):
    saida = [0 for _ in range(3)]
    for j in range(3):
        for i in range(4):
            saida[j] += W[i][j] * x[i]
    return saida

def cosseno(a, b):
    numerador = sum(a[i] * b[i] for i in range(len(a)))
    norma_a = sum(x**2 for x in a) ** 0.5
    norma_b = sum(x**2 for x in b) ** 0.5
    if norma_a == 0 or norma_b == 0:
        return 0
    return numerador / (norma_a * norma_b)

x1 = [X[i][0] for i in range(4)]
t1 = [T[i][0] for i in range(3)]

saida = lembrar(x1)

print("\nEntrada (Rosto 1):", x1)
print("Saída esperada (João):", t1)
print("Saída da rede:", saida)
print("Cosseno de semelhança:", round(cosseno(saida, t1), 4))
