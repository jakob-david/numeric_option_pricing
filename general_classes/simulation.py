from other_methods.Analytic import Analytic
from other_methods.MonteCarlo import MonteCarlo
from finite_difference_methods.CrankNicolson import CrankNicolson
from finite_difference_methods.ImplicitFD import ImplicitFD

import matplotlib.pyplot as plt
import numpy as np


class Simulation:

    def __init__(self, stock):
        self.stock = stock

    # calculate methods
    # --------------------------------------
    def calculate_analytic(self):
        method = Analytic(self.stock)
        return method.calculate()

    def calculate_monte_carlo(self, n):
        method = MonteCarlo(self.stock)
        return method.calculate(n)


