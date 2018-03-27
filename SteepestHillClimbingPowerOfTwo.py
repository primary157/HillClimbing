from SteepestHillClimbing import SteepestHillClimbing


class SteepestHillClimbingPowerOfTwo(SteepestHillClimbing):
    def __init__(self, min, max, p):
        SteepestHillClimbing.__init__(self, min, max, p, 1)

    def function(self, n):
        return n[0] ** 2
