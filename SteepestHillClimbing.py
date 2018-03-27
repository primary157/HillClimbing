import random


def generate_random(min, max):
    return (max - min) * random.Random().random() + min


class SteepestHillClimbing:
    def __init__(self, min, max, p, l):
        self.min = [min] * l
        self.max = [max] * l
        self.p = p
        self.l = l

    def function(self, n):
        raise NotImplementedError("Please Implement this method with a testing function!")

    def init(self):
        v = [None] * self.l
        for i in range(self.l):
            v[i] = generate_random(self.min[i], self.max[i])
        return v

    def tweak(self, v):
        r = [None] * self.l
        for i in range(self.l):
            if self.p >= generate_random(0, 1):
                while True:
                    r[i] = generate_random(v[i] * 0.95, v[i] * 1.05)  # add noise of +/- 5%
                    if self.min[i] <= r[i] <= self.max[i]:  # test limits
                        break
                v[i] = r[i]
        return v

    def compare(self, a, b):
        return self.function(a) > self.function(b)

    def run(self):
        v = self.init()  # Initial random candidate solution
        failed = 0
        tweaks = 100  # Desired Number of tweaks
        while failed < 10:
            r = self.tweak(v.copy())
            for _ in range(tweaks - 1):
                w = self.tweak(v.copy())
                if self.compare(w, r):
                    r = w
            if self.compare(r, v):
                v = r
                failed = 0  # Value changed!
            else:
                failed += 1  # Times without changing value
        return v, self.function(v)  # return variables and function!
