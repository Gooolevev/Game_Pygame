import random

class PerlinNoise:
    def __init__(self, seed=None):
        local_rng = random.Random(seed)
        random.seed(seed)

        self.p = list(range(256))
        local_rng.shuffle(self.p)
        self.p = self.p * 2

    def fade(self, t):
        """S-кривая"""
        return 6*t**5 - 15*t**4 + 10*t**3

    def lerp(self, t, a, b):
        return a + t * (b - a)

    def grad(self, hash_code, x, y):
        h = hash_code & 7
        if h == 0: return  x + y
        if h == 1: return -x + y
        if h == 2: return  x - y
        if h == 3: return -x - y
        if h == 4: return  x
        if h == 5: return -x
        if h == 6: return  y
        if h == 7: return -y
        return 0

    def noise(self, x, y):
        xi = int(x) & 255
        yi = int(y) & 255
        
        xf = x - int(x)
        yf = y - int(y)
        
        u = self.fade(xf)
        v = self.fade(yf)
        
        p = self.p
        aa = p[p[xi] + yi]
        ab = p[p[xi] + yi + 1]
        ba = p[p[xi + 1] + yi]
        bb = p[p[xi + 1] + yi + 1]
        
        x1 = self.lerp(u, self.grad(aa, xf, yf), self.grad(ba, xf - 1, yf))
        x2 = self.lerp(u, self.grad(ab, xf, yf - 1), self.grad(bb, xf - 1, yf - 1))
        