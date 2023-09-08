import numpy as np
import matplotlib.pyplot as plt

from other_methods.Analytic import Analytic
from other_methods.MonteCarlo import MonteCarlo
from other_methods.BinomialTree import BinomialTree
from other_methods.TrinomialTree import TrinomialTree

from finite_difference_methods.CrankNicolson import CrankNicolson
from finite_difference_methods.ImplicitFD import ImplicitFD
from finite_difference_methods.ExplicitFD import ExplicitFD


class Simulation:

    def __init__(self, stock):
        self.stock = stock

    # calculate methods
    # --------------------------------------
    def calculate_analytic(self):
        """
        Calculates the stock price after t time analytically.

        :return: stock price
        """

        method = Analytic(self.stock)
        return method.calculate()

    def calculate_monte_carlo(self, n):
        """
        Calculates the stock price after t time using a Monte-Carlo simulation.

        :param n: number of runs

        :return: stock price
        """

        method = MonteCarlo(self.stock)
        return method.calculate(n)

    def calculate_binomial_tree(self, n):
        """
        Calculates the stock price after t time using a binomial tree simulation.

        :param n: number of time steps

        :return: stock price
        """

        method = BinomialTree(self.stock)
        return method.calculate(n)

    def calculate_trinomial_tree(self, n):
        """
        Calculates the stock price after t time using a trinomial tree simulation.

        :param n: number of time steps

        :return: stock price
        """

        method = TrinomialTree(self.stock)
        return method.calculate(n)

    def calculate_explicit_fd(self, n_s, n_t, bc):
        """
        Calculates the stock price after t time using the explicit finite difference method.

        :param n_s: number of spot prices
        :param n_t: number of time steps
        :param bc: the type of border conditions. (d...Dirichlet, n...von Neumann)

        :return: stock price
        """

        method = ExplicitFD(self.stock)
        return method.calculate(n_s, n_t, bc)

    def calculate_implicit_fd(self, n_s, n_t, bc):
        """
        Calculates the stock price after t time using the implicit finite difference method.

        :param n_s: number of spot prices
        :param n_t: number of time steps
        :param bc: the type of border conditions. (d...Dirichlet, n...von Neumann)

        :return: stock price
        """

        method = ImplicitFD(self.stock)
        return method.calculate(n_s, n_t, bc)

    def calculate_crank_nicolson(self, n_s, n_t, bc):
        """
        Calculates the stock price after t time using the Crank-Nicolson method.

        :param n_s: number of spot prices
        :param n_t: number of time steps
        :param bc: the type of border conditions. (d...Dirichlet, n...von Neumann)

        :return: stock price
        """

        method = CrankNicolson(self.stock)
        return method.calculate(n_s, n_t, bc)

    # plot functions
    # --------------------------------------
    def plot_explicit_fd(self, ns_min, ns_max, nt_min, nt_max, bc, difference=True):
        """
        Plots the solutions of the explicit finite difference method for different spot prices and different time steps.

        :param ns_min: minimum spot prices
        :param ns_max: maximum spot prices
        :param nt_min: minimum time steps
        :param nt_max: maximum time steps
        :param bc: the type of border conditions (d...Dirichlet, n...von Neumann)
        :param difference: false...prices are visible; true...differences to analytic solution are visible

        :return: plot
        """

        self.plot_fd(ns_min, ns_max, nt_min, nt_max, bc, difference, ExplicitFD(self.stock).calculate)

    def plot_implicit_df(self, ns_min, ns_max, nt_min, nt_max, bc, difference=True):
        """
        Plots the solutions of the implicit finite difference method for different spot prices and different time steps.

        :param ns_min: minimum spot prices
        :param ns_max: maximum spot prices
        :param nt_min: minimum time steps
        :param nt_max: maximum time steps
        :param bc: the type of border conditions (d...Dirichlet, n...von Neumann)
        :param difference: false...prices are visible; true...differences to analytic solution are visible

        :return: plot
        """

        self.plot_fd(ns_min, ns_max, nt_min, nt_max, bc, difference, ImplicitFD(self.stock).calculate)

    def plot_crank_nicolson(self, ns_min, ns_max, nt_min, nt_max, bc, difference=True):
        """
        Plots the solutions of the Crank-Nicolson method for different spot prices and different time steps.

        :param ns_min: minimum spot prices
        :param ns_max: maximum spot prices
        :param nt_min: minimum time steps
        :param nt_max: maximum time steps
        :param bc: the type of border conditions (d...Dirichlet, n...von Neumann)
        :param difference: false...prices are visible; true...differences to analytic solution are visible

        :return: plot
        """

        self.plot_fd(ns_min, ns_max, nt_min, nt_max, bc, difference, CrankNicolson(self.stock).calculate)

    def plot_monte_carlo(self, nt_min, nt_max, difference=True):
        """
        Plots the solutions of the Monte-Carlo method for different numbers of runs.

        :param nt_min: minimum time steps
        :param nt_max: maximum time steps
        :param difference: false...prices are visible; true...differences to analytic solution are visible

        :return: plot
        """

        if nt_min < 1:
            print("Error: minimum is one run")
            return

        self.plot(nt_min, nt_max, difference, MonteCarlo(self.stock).calculate)

    def plot_binomial_tree(self, nt_min, nt_max, difference=True):
        """
        Plots the solutions of the binomial tree method for different time steps.

        :param nt_min: minimum time steps
        :param nt_max: maximum time steps
        :param difference: false...prices are visible; true...differences to analytic solution are visible

        :return: plot
        """

        if nt_min < 1:
            print("Error: minimum is one timestep")
            return

        self.plot(nt_min, nt_max, difference, BinomialTree(self.stock).calculate)

    def plot_trinomial_tree(self, nt_min, nt_max, difference=True):
        """
        Plots the solutions of the trinomial tree method for different time steps.

        :param nt_min: minimum time steps
        :param nt_max: maximum time steps
        :param difference: false...prices are visible; true...differences to analytic solution are visible

        :return: plot
        """

        if nt_min < 1:
            print("Error: minimum is one timestep")
            return

        self.plot(nt_min, nt_max, difference, TrinomialTree(self.stock).calculate)

    # plot helper functions
    # --------------------------------------
    def plot(self, nt_min, nt_max, difference, function):
        """
        Actually handles the plotting for the "other methods".

        :param nt_min: minimum time steps
        :param nt_max: maximum time steps
        :param difference: false...prices are visible; true...differences to analytic solution are visible
        :param function: the function which is plotted. (the numeric method)

        :return: plot
        """

        if difference:
            analytic = Analytic(self.stock).calculate()
        else:
            analytic = 0

        y = np.zeros(nt_max-nt_min+1)
        x = np.zeros(nt_max-nt_min+1)

        for i in range(nt_min, nt_max+1):
            y[i-1] = function(i) - analytic
            x[i-1] = i

        plt.plot(x, y)

        plt.xlabel("number of time steps")
        if difference:
            plt.ylabel("difference")
        else:
            plt.ylabel("price")

        plt.show()
        plt.close()

    def plot_fd(self, ns_min, ns_max, nt_min, nt_max, bc, difference, function):
        """
        Actually handles the plotting routine for finite difference methods.

        :param ns_min: minimum spot prices
        :param ns_max: maximum spot prices
        :param nt_min: minimum time steps
        :param nt_max: maximum time steps
        :param bc: the type of border conditions (d...Dirichlet, n...von Neumann)
        :param difference: false...prices are visible; true...differences to analytic solution are visible
        :param function: the function which is plotted. (the numeric method)

        :return: plot
        """

        if nt_min < 1:
            print("Error: minimum is one time step")
            return

        if ns_min < 1:
            print("Error: minimum is one spot price")
            return

        matrix = np.zeros((ns_max-ns_min+1, nt_max-nt_min+1))

        if difference:
            analytic = Analytic(self.stock).calculate()
        else:
            analytic = 0

        for s in range(ns_min, ns_max+1):
            for t in range(nt_min, nt_max+1):
                matrix[s-1][t-1] = function(s, t, bc) - analytic

        x = np.arange(nt_min, nt_max+1)
        y = np.arange(ns_min, ns_max+1)

        x, y = np.meshgrid(x, y)
        z = matrix

        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        # Plot a basic wireframe.
        ax.plot_wireframe(x, y, z, rstride=1, cstride=1)

        plt.xlabel("number of time steps")
        plt.ylabel("number of spot prices")

        if difference:
            ax.set_zlabel("difference")
        else:
            ax.set_zlabel("price")

        plt.show()
        plt.close()
