import math
from scipy.stats import norm


class Analytic:

    def __init__(self, stock):
        """
        Solves the Black–Scholes equation analytically.

        :param stock: The stock for witch the future price should be calculated. (class Stock)
        """

        self.stock = stock

    def calculate(self):
        """
        Calculates the price analytically.

        :return: The price after t time.
        """

        s = self.stock.S
        k = self.stock.K
        t = self.stock.T
        r = self.stock.r
        d = self.stock.d
        vol = self.stock.v

        d1 = (math.log(s / k) + ((r - d) + vol * vol / 2) * t) / (vol * t ** 0.5)
        d2 = (math.log(s / k) + ((r - d) - vol * vol / 2) * t) / (vol * t ** 0.5)

        if 'call' == self.stock.kind:
            return s * math.exp(-d * t) * norm.cdf(d1) - k * math.exp(-r * t) * norm.cdf(d2)
        elif 'put' == self.stock.kind:
            return k * math.exp(-r * t) * norm.cdf(-d2) - s * math.exp(-d * t) * norm.cdf(-d1)
        else:
            return False
