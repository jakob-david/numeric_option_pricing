import math

from finite_difference_methods.FiniteDifference import FiniteDifference


class CrankNicolson(FiniteDifference):

    def __init__(self, stock):
        """
        Solves the Black–Scholes equation using the Crank-Nicolson method.

        :param stock: The stock for witch the future price should be calculated. (class Stock)
        """

        self.stock = stock

    def calculate(self, n_s, n_t, bc):

        s, k, t, r, q, sigma = self.get_parameters_form_stock(self.stock)
        smax, n_s, dt, ds = self.get_parameters(n_s, n_t, s, t, sigma)

        fm, g, a, b, c, as_, bs, cs = self.get_arrays(n_s, 8)

        f = self.get_f_array(n_s, ds, k, self.stock.kind)

        sigma_sq = sigma * sigma
        q = 0  # possible improvement

        for j in range(0, n_s + 1):
            a[j] = -.25 * j * dt * (j * sigma_sq - r)
            b[j] = 1 + .5 * dt * (j * j * sigma_sq + r)
            c[j] = -.25 * j * dt * (j * sigma_sq + r)

            as_[j] = .25 * j * dt * (j * sigma_sq - r)
            bs[j] = 1 - .5 * dt * (j * j * sigma_sq + r)
            cs[j] = .25 * j * dt * (j * sigma_sq + r)

        if "n" == bc:
            # Nemann Impl
            b[0] = b[0] + 2 * a[0]
            c[0] = c[0] - a[0]

            b[n_s] = b[n_s] + 2 * c[n_s]
            a[n_s] = -c[n_s] + a[n_s]

            # Nemann Expl
            bs[0] = bs[0] + 2 * as_[0]
            cs[0] = -as_[0] + cs[0]

            bs[n_s] = bs[n_s] + 2 * cs[n_s]
            as_[n_s] = as_[n_s] - cs[n_s]
        else:
            # not Neumann
            a[0] = 0
            b[0] = 1
            c[0] = 0

            c[n_s] = 0
            b[n_s] = 1
            a[n_s] = 0

        if 'n' == bc:  # Neuman Condition
            for i in range(n_t, 0, -1):
                g[0] = f[0] * b[0] + f[1] * c[0]  # Die Randbedinungen müssen manuel gesetzt werden.
                g[n_s] = f[n_s] * b[n_s] + f[n_s - 1] * a[n_s]
                for j in range(1, n_s):
                    g[j] = as_[j] * f[j - 1] + bs[j] * f[j] + cs[j] * f[j + 1]
                self.tridag(a, b, c, g, fm, n_s + 1)
                for j in range(0, n_s + 1):
                    f[j] = fm[j]
        elif 'd' == bc and 'call' == self.stock.kind:  # Dirichlet Condition for call
            for i in range(n_t, 0, -1):
                g[0] = 0
                g[n_s] = smax - k * math.exp(-r * (t - dt * i))
                for j in range(1, n_s):
                    g[j] = as_[j] * f[j - 1] + bs[j] * f[j] + cs[j] * f[j + 1]
                self.tridag(a, b, c, g, fm, n_s + 1)
                for j in range(1, n_s):
                    f[j] = fm[j]
                f[0] = 0
                f[n_s] = smax - k * math.exp(-r * (t - dt * i))
        elif 'd' == bc and 'put' == self.stock.kind:  # Dirichlet Condition for call
            for i in range(n_t, 0, -1):
                g[0] = k * math.exp(-r * (t - dt * i))
                g[n_s] = 0
                for j in range(1, n_s):
                    g[j] = as_[j] * f[j - 1] + bs[j] * f[j] + cs[j] * f[j + 1]
                self.tridag(a, b, c, g, fm, n_s + 1)
                for j in range(1, n_s):
                    f[j] = fm[j]
                f[0] = k * math.exp(-r * (t - dt * i))
                f[n_s] = 0
        elif 'm' == bc:  # my own solution
            for i in range(n_t, 0, -1):
                g[0] = f[0] * math.exp(r * dt)
                g[n_s] = f[n_s] * math.exp(r * dt)
                for j in range(1, n_s):
                    g[j] = as_[j] * f[j - 1] + bs[j] * f[j] + cs[j] * f[j + 1]
                self.tridag(a, b, c, g, fm, n_s + 1)
                for j in range(1, n_s):
                    f[j] = fm[j]
                f[0] = f[0] * math.exp(r * dt)
                f[n_s] = f[n_s] * math.exp(r * dt)
        elif '' == bc:  # no discounting
            for i in range(n_t, 0, -1):
                g[0] = f[0]
                g[n_s] = f[n_s]
                for j in range(1, n_s):
                    g[j] = as_[j] * f[j - 1] + bs[j] * f[j] + cs[j] * f[j + 1]
                self.tridag(a, b, c, g, fm, n_s + 1)
                for j in range(0, n_s + 1):
                    f[j] = fm[j]

        else:
            return False

        return f[int(n_s / 2)]