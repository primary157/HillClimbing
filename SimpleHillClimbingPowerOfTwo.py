from SteepestHillClimbingPowerOfTwo import SteepestHillClimbingPowerOfTwo


class SimpleHillClimbingPowerOfTwo(SteepestHillClimbingPowerOfTwo):
    def run(self):
        v = self.init()  # Initial random candidate solution
        failed = 0
        while failed < 10:
            r = self.tweak(v.copy())
            if self.compare(r, v):
                v = r
                failed = 0  # Value changed!
            else:
                failed += 1  # Times without changing value
        return v, self.function(v)  # return variables and function!
