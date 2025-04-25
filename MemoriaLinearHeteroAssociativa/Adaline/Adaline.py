import random

# Dados de entrada (6 características x 9 amostras)
X = [
    [1, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 1, 0, 0, 0, 0]
]

# Saídas (3 categorias x 9 amostras)
T = [
    [0, 0, 0, 0, 0, 0, 1, 1, 1],  # "croustillant"
    [1, 1, 1, 0, 0, 0, 0, 0, 0],  # "craquant"
    [0, 0, 0, 1, 1, 1, 0, 0, 0]   # "croquant"
]

eta = 0.01
epochs = 300
n_inputs = 6
n_outputs = 3
n_samples = 9

# Inicializar pesos aleatórios (6x3)
W = [[random.uniform(-0.6, 0.6) for _ in range(n_outputs)] for _ in range(n_inputs)]

#Calcula a saída O = W^t * X
def calcular_saida(W, X):
    O = [[0.0 for _ in range(n_samples)] for _ in range(n_outputs)]
    for j in range(n_outputs):
        for i in range (n_samples):
            soma = 0.0
            for k in range(n_inputs):
                soma += W[k][j] * X[k][i]
            O[j][i] = soma
    return O

#Treinamento
for epoch in range(epochs):
    O = calcular_saida(W, X)
    
    #Calcula erro E = T - O
    E = [[T[j][i] - O[j][i] for i in range(n_samples)] for j in range(n_outputs)]
    
    #Atualizar pesos: W += eta * X * E^t
    for i in range(n_inputs):
        for j in range(n_outputs):
            soma = 0.0
            for k in range(n_samples):
                soma += X[i][k] * E[j][k]
            W[i][j] += eta * soma
            
    #Erro quadrático total
    erro_total = sum(E[j][i]**2 for j in range(n_outputs) for i in range(n_samples))
    if epoch % 50 == 0 or epoch == epochs - 1:
        print(f"Época {epoch+1}, erro quadrático: {round(erro_total, 4)}")
    
#Resultado final
print("\nPesos finais:")
for linha in W:
    print([round(v, 4) for v in linha])
    
print("\Saída final (O):")
O_final = calcular_saida(W, X)
for linha in O_final:
    print([round(v, 2) for v in linha])