import random


def generate_random(min, max):
    return (max - min) * random.Random().random() + min


class SteepestHillClimbing:
    def __init__(self, min, max, p, l, func, bigger):
        self.min = [min] * l
        self.max = [max] * l
        self.l = l
        self.p = p
        self.func = func
        self.wants_bigger = bigger  # user wants bigger

    def init(self):
        v = [None]*self.l
        for i in range(self.l):
            v[i] = generate_random(self.min[i], self.max[i])
        return v

    def tweak(self, v):
        r = [None]*self.l
        for i in range(self.l):
            if p >= generate_random(0, 1):
                while True:
                    r[i] = generate_random(v[i] * 0.95, v[i] * 1.05)  # add noise of 5%
                    # n = generate_random(-r[i], r[i])
                    if self.min[i] <= r[i] <= self.max[i]:
                        break
                v[i] = r[i]
        return v

    def quality(self, v):
        import numpy
        a = [self.func(v)]
        return numpy.sum(a)

    def compare(self, a, b):
        if self.wants_bigger:
            self.quality(a) > self.quality(b)
        else:
            self.quality(a) < self.quality(b)

    def run(self):
        v = self.init()
        failed = 0
        tweaks = 1000
        while failed < 100:
            r = self.tweak(v.copy())
            for _ in range(tweaks - 1):
                w = self.tweak(v.copy())
                if self.compare(w, r):
                    r = w
            if self.compare(r, v):
                v = r
                failed = 0
            else:
                failed += 1  # Conta quantas vezes permaneceu inalterado
        return v, self.func(v)


def n_quadrado(n):
    return n[0] ** 2


def rastringin(n):
    from math import cos
    from math import pi
    return 20 + (n[0] ** 2) + (n[1] ** 2) - 10 * (cos(2 * pi * n[0]) + cos(2 * pi * n[1]))


if __name__ == "__main__":
    print('''1) n²
2) Rastringin''')
    resposta = int(input("Qual função em que deseja testar? "))
    prioridade = bool(input("Digite 1 se quiser encontrar o maior valor e 0 se quiser o menor:"))
    p = 1  # Probabilidade de não ter ruído
    if resposta == 1:
        func = n_quadrado
        l = 1  # Número de variáveis
    else:
        func = rastringin
        l = 2  # Número de variáveis
    min = -10
    max = 10
    hc = SteepestHillClimbing(min, max, p, l, func, prioridade)
    for i in hc.run():
        print(i)
