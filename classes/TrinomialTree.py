import math


class TrinomialTree:

    def __init__(self, stock):
        """
        Solves the Black–Scholes equation using a trinomial tree simulation.

        :param stock: The stock for witch the future price should be calculated. (class Stock)
        """

        self.stock = stock

    def calculate(self, N):

        S = self.stock.S
        K = self.stock.K
        t = self.stock.T
        r = self.stock.r
        q = self.stock.d
        sigma = self.stock.v

        dt = t / N
        sigma_sqr = sigma * sigma

        u = math.exp(sigma * math.sqrt(3 * dt))
        d = 1 / u
        p_u = 1 / 6 + math.sqrt(dt / (12 * sigma_sqr)) * (r - q - 0.5 * sigma_sqr)
        p_m = 2 / 3
        p_d = 1 / 6 - math.sqrt(dt / (12 * sigma_sqr)) * (r - q - 0.5 * sigma_sqr)
        C = {}

        if 'call' == self.stock.kind:
            for m in range(0, N * 2 + 1):
                C[(N, m)] = max(S * (u ** (m - N)) - K, 0)

        elif 'put' == self.stock.kind:
            for m in range(0, N * 2 + 1):
                C[(N, m)] = max(K - S * (u ** (m - N)), 0)

        else:
            return False

        for k in range(N - 1, -1, -1):
            for m in range(0, k + k + 1):
                C[(k, m)] = math.exp(-r * dt) * (
                            p_u * C[(k + 1, m + 2)] + p_m * C[(k + 1, m + 1)] + p_d * C[(k + 1, m)])
        return C[(0, 0)]
