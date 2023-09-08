import math

import numpy as np


class FiniteDifference:

    @staticmethod
    def get_parameters_form_stock(stock):
        """
        Gets relevant parameters from the class Stock and saves them into variables.

        :param stock: The Stock object.

        Returns: Tuple
            - s - spot price
            - k - strike price
            - t - time
            - r - risk-free interest rate
            - q - dividend
            - sigma - volatility
        """

        s = stock.S
        k = stock.K
        t = stock.T
        r = stock.r
        q = stock.d
        sigma = stock.v

        return s, k, t, r, q, sigma

    def get_parameters(self, n_s, n_t, s, t, sigma):
        """
        Calculates important parameters.

        :param n_s: number of spot prices
        :param n_t: number of times
        :param s: spot price
        :param t: time
        :param sigma: volatility

        Returns: Tuple
            - smax - maximum spot price
            - n_s - corrected number of spot prices
            - dt - length of one time step
            - ds - the spacing of the spot prices
        """

        smax = 2 * s

        if n_s is not False:
            n_s = self.calculate_ns(n_t, smax, sigma, t)
            n_s = n_s + (n_s % 2)
        else:
            n_s = n_s + (n_s % 2)

        n_s = int(n_s)

        dt = t / n_t
        ds = 2 * s / n_s

        return smax, n_s, dt, ds

    @staticmethod
    def get_arrays(size, number):
        """
        Gets a defined number of arrays in a defined size.

        :param size: size of the array
        :param number: number of arrays

        :return: the arrays inside a tuple.
        """

        ret = list()
        for i in range(0, number):
            ret.append([0] * (size + 1))

        return tuple(ret)

    @staticmethod
    def get_initial_array(size, ds, k, kind):
        """
        Initializes the arrays with the initial conditions.

        :param size: the size of the arrays.
        :param ds: the spacing of the spot prices.
        :param k: the strike price
        :param kind: the kind of the option (put or call)

        :return: the array with the initial conditions.
        """

        f = [0] * (size + 1)

        if 'call' == kind:
            for j in range(0, size + 1):
                s = j * ds
                f[j] = max(s - k, 0)  # here you can omit the loop.
        elif 'put' == kind:
            for j in range(0, size + 1):
                s = j * ds
                f[j] = max(k - s, 0)  # here you can omit the loop.
        else:
            return False

        return f

    @staticmethod
    def calculate_ns(n_t, smax, volatility, t):
        return int(math.log(smax) / (volatility * math.sqrt(3 * (t / n_t))))

    @staticmethod
    def tridag(d1, d2, d3, b, x, n):
        """
        Solves a System ol linear equations Ax=b where A is a tri-diagonal matrix.
        The input vector is not modified.

        :param d1: first diagonal
        :param d2: second diagonal
        :param d3: third diagonal
        :param b: the inhomogeneity.
        :param x: the vector for which is solved for.
        :param n: the size of the system.

        :return: the solution vector x
        """

        gam = [0] * n

        if d2[0] == 0.0:
            return False

        bet = d2[0]
        x[0] = b[0] / bet

        for j in range(1, n):
            gam[j] = d3[j - 1] / bet
            bet = d2[j] - d1[j] * gam[j]

            if bet == 0.0:
                return False

            x[j] = (b[j] - d1[j] * x[j - 1]) / bet

        for j in range(n - 2, 0, -1):
            x[j] -= gam[j + 1] * x[j + 1]

        return x
