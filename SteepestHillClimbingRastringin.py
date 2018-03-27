from SteepestHillClimbing import SteepestHillClimbing


class SteepestHillClimbingRastringin(SteepestHillClimbing):
    def __init__(self, min, max, p):
        SteepestHillClimbing.__init__(self, min, max, p, 2)  # Rastringin is a two variables function

    def function(self, n):  # Rastringin
        from math import cos
        from math import pi
        return 20 + (n[0] ** 2) + (n[1] ** 2) - 10 * (cos(2 * pi * n[0]) + cos(2 * pi * n[1]))

    def compare(self, a, b):  # Minimize in spite of maximize
        return self.function(a) < self.function(b)
