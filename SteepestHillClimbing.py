'''
BSD 3-Clause License

Copyright (c) 2018, Victor Guerra Veloso
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''
import random


def generate_random(min, max):
    return (max - min) * random.Random().random() + min


'''
Base class for SteepestHillClimbing metaheuristics
'''
class SteepestHillClimbing:
    def __init__(self, min, max, p, l):
        self.min = [min] * l  # All axis limits are the same in my implementation for easy of use
        self.max = [max] * l
        self.p = p
        self.l = l

    def function(self, n):
        raise NotImplementedError("Please Implement this method with a testing function!")

    def init(self):  # Initialize random candidate solution
        v = []
        for i in range(self.l):
            v.append(generate_random(self.min[i], self.max[i]))
        return v

    def tweak(self, v):
        r = [None] * self.l  # Initialize empty vector
        for i in range(self.l):  # For each variable
            if self.p >= generate_random(0, 1):  # Check if it should tweak
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
