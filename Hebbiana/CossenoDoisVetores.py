#CossenoDoisVetores

X = [
    [1, -1, -1, 1, -1, 1, 1, -1, -1, 1],
    [1, -1, -1, -1, 1, -1, 1, -1, 1, 1],
    [1, 1, -1, -1, -1, 1, 1, -1, 1, -1],
    [-1, -1, -1, 1, -1, 1, 1, 1, -1, 1]
]

O = [
    [8, -16, -20, 12, -16, 16, 10, -8, -12, 16],
    [16, -8, -12, -12, 8, -8, 12, -16, 12, 8],
    [16, 8, -12, -12, -8, 8, 12, -16, 12, -8],
    [-8, -16, -12, 20, -16, 16, 12, 8, -20, 16]
]

cosseno = [0 for _ in range(10)]
for i in range(10):
    cosseno[i]=0
    print()

for j in range(10):
    for i in range(4):
        cosseno[j]=cosseno[j]+O[i][j]*X[i][j]
        print()
    print()

for i in range(10):
    print(f"{cosseno[i]:8.4f}", end = " ")