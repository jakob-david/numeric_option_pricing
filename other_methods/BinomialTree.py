import math


class BinomialTree:

    def __init__(self, stock):
        """
        Solves the Black–Scholes equation using a binomial tree simulation.

        :param stock: The stock for witch the future price should be calculated. (class Stock)
        """

        self.stock = stock

    def calculate(self, n):
        """
        Calculates the price using a binomial tree simulation.

        :param n: The number of simulation steps.

        :return: The price after t time.
        """

        s = self.stock.s
        k = self.stock.k
        t = self.stock.t
        r = self.stock.r
        d = self.stock.d
        vol = self.stock.v

        dt = t / n
        u = math.exp(vol * math.sqrt(dt))
        d = 1 / u
        p = (math.exp(r * dt) - d) / (u - d)
        c = {}

        if 'call' == self.stock.kind:
            for m in range(0, n + 1):
                c[(n, m)] = max(s * (u ** (2 * m - n)) - k, 0)

        elif 'put' == self.stock.kind:
            for m in range(0, n + 1):
                c[(n, m)] = max(k - s * (u ** (2 * m - n)), 0)

        else:
            return False

        for k in range(n - 1, -1, -1):
            for m in range(0, k + 1):
                c[(k, m)] = math.exp(-r * dt) * (p * c[(k + 1, m + 1)] + (1 - p) * c[(k + 1, m)])
        return c[(0, 0)]
