from SteepestHillClimbingPowerOfTwo import SteepestHillClimbingPowerOfTwo
from SteepestHillClimbingRastringin import SteepestHillClimbingRastringin

if __name__ == "__main__":
    resultados = []
    min = -10
    max = 10
    resposta = int(input("Qual função deseja testar? (1-Quadrática 2-Rastringin): "))
    p = float(input("Qual probabilidade de ter ruído? (0,1] "))  # Probabilidade de ter ruído
    if resposta == 1:
        hc = SteepestHillClimbingPowerOfTwo(min, max, p)
    else:
        hc = SteepestHillClimbingRastringin(min, max, p)
    for j in range(10):
        resultados.append(hc.run()[1])
    import numpy as np

    print(np.mean(resultados))  # pega a média de 1000 execuções
    print(resultados)  # pega a média de 1000 execuções
