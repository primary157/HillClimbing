import numpy as np

from SimpleHillClimbingPowerOfTwo import SimpleHillClimbingPowerOfTwo
from SteepestHillClimbingPowerOfTwo import SteepestHillClimbingPowerOfTwo
from SteepestHillClimbingRastringin import SteepestHillClimbingRastringin

if __name__ == "__main__":
    resultados = []
    min = float(input("Qual limite inferior para x? "))
    max = float(input("Qual limite superior para x? "))
    resposta = int(input(
        "Qual função deseja testar? (1-Quadrática(com uma amostra) 2-Quadrática(com muitas amostras) 3-Rastringin): "))
    p = float(input("Qual probabilidade de ter ruído? (0,1] "))  # Noise probability
    if resposta == 1:
        hc = SimpleHillClimbingPowerOfTwo(min, max, p)
    elif resposta == 2:
        hc = SteepestHillClimbingPowerOfTwo(min, max, p)
    else:
        hc = SteepestHillClimbingRastringin(min, max, p)
    for j in range(100):
        resultados.append(hc.run()[1])

    print(np.mean(resultados))  # Print mean of the results
    print(resultados)  # Print results
