import math
from scipy.stats import norm
import random


class MonteCarlo:

    def __init__(self, stock):
        """
        Solves the Black–Scholes equation using a Monte-Carlo simulation.

        :param stock: The stock for witch the future price should be calculated. (class Stock)
        """

        self.stock = stock

    def calculate(self, n):
        """
        Calculates the price using a Monte-Carlo Simulation.

        :param n: The number of simulation runs.

        :return: The price after t time.
        """

        s = self.stock.s
        k = self.stock.k
        t = self.stock.t
        r = self.stock.r
        d = self.stock.d
        vol = self.stock.v

        sum_price = 0

        if 'call' == self.stock.kind:
            for j in range(2, n):
                stock_price = s * math.exp((r - vol * vol / 2) * t + vol * norm.ppf(random.uniform(0, 1)) * math.sqrt(t))
                option_price = math.exp(-r * t) * max(stock_price - k, 0)

                sum_price = sum_price + option_price

        elif 'put' == self.stock.kind:
            for j in range(2, n):
                stock_price = s * math.exp((r - vol * vol / 2) * t + vol * norm.ppf(random.uniform(0, 1)) * math.sqrt(t))
                option_price = math.exp(-r * t) * max(k - stock_price, 0)

                sum_price = sum_price + option_price

        else:
            return False

        return sum_price / n

