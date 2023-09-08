import math


class TrinomialTree:

    def __init__(self, stock):
        """
        Solves the Black–Scholes equation using a trinomial tree simulation.

        :param stock: The stock for witch the future price should be calculated. (class Stock)
        """

        self.stock = stock

    def calculate(self, n):
        """
        Calculates the price using a trinomial tree simulation.

        :param n: The number of simulation steps.

        :return: The price after t time.
        """

        s = self.stock.s
        k = self.stock.k
        t = self.stock.t
        r = self.stock.r
        q = self.stock.d
        sigma = self.stock.v

        dt = t / n
        sigma_sqr = sigma * sigma

        u = math.exp(sigma * math.sqrt(3 * dt))
        # d = 1 / u
        p_u = 1 / 6 + math.sqrt(dt / (12 * sigma_sqr)) * (r - q - 0.5 * sigma_sqr)
        p_m = 2 / 3
        p_d = 1 / 6 - math.sqrt(dt / (12 * sigma_sqr)) * (r - q - 0.5 * sigma_sqr)
        c = {}

        if 'call' == self.stock.kind:
            for m in range(0, n * 2 + 1):
                c[(n, m)] = max(s * (u ** (m - n)) - k, 0)

        elif 'put' == self.stock.kind:
            for m in range(0, n * 2 + 1):
                c[(n, m)] = max(k - s * (u ** (m - n)), 0)

        else:
            return False

        for k in range(n - 1, -1, -1):
            for m in range(0, k + k + 1):
                c[(k, m)] = math.exp(-r * dt) * (
                            p_u * c[(k + 1, m + 2)] + p_m * c[(k + 1, m + 1)] + p_d * c[(k + 1, m)])
        return c[(0, 0)]
