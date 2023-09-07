import math
from classes.FiniteDifference import FiniteDifference


class ImplicitFD(FiniteDifference):

    def __init__(self, stock):
        """
        Solves the Black–Scholes equation using an implicit finite difference method.

        :param stock: The stock for witch the future price should be calculated. (class Stock)
        """

        self.stock = stock

    def calculate(self, n_s, n_t, bc):
        """
        Calculates the price using an implicit finite difference method.

        :param n_s: The number of starting prices.
        :param n_t: The number of time steps.
        :param bc:  The type of border conditions. (d...Dirichlet, n...von Neumann)

        :return: The price of the stock after t time.
        """

        s = self.stock.S
        k = self.stock.K
        t = self.stock.T
        r = self.stock.r
        q = self.stock.d
        sigma = self.stock.v

        smax = 2 * s

        if n_s:
            n_s = self.calcNS(n_t, smax, sigma, t)
            n_s = n_s + (n_s % 2)
        else:
            n_s = n_s + (n_s % 2)

        n_s = int(n_s)

        dt = t / n_t
        ds = smax / n_s

        f = [0] * (n_s + 1)
        a = [0] * (n_s + 1)
        b = [0] * (n_s + 1)
        c = [0] * (n_s + 1)
        fm = [0] * (n_s + 1)

        # print(n_s)
        # q = 0 # possible addition

        if 'call' == self.stock.kind:
            for j in range(0, n_s + 1):
                s = j * ds
                f[j] = max(s - k, 0)  # here you can omit the loop.
        elif 'put' == self.stock.kind:
            for j in range(0, n_s + 1):
                s = j * ds
                f[j] = max(k - s, 0)  # here you can omit the loop.
        else:
            return False

        # tri-diagonal matrix initialisation
        for j in range(0, n_s + 1):
            a[j] = .5 * dt * ((r - q) * j - sigma * sigma * j * j)
            b[j] = 1 + sigma * sigma * j * j * dt + r * dt
            c[j] = .5 * dt * (-(r - q) * j - sigma * sigma * j * j)

        if "n" == bc:
            # Von Neumann
            b[0] = b[0] + 2 * a[0]
            c[0] = c[0] - a[0]

            b[n_s] = b[n_s] + 2 * c[n_s]
            a[n_s] = c[n_s] - a[n_s]
        else:
            # not von Neumann
            a[0] = 0
            b[0] = 1
            c[0] = 0

            c[n_s] = 0
            b[n_s] = 1
            a[n_s] = 0

        if 'n' == bc:  # Neumann Condition
            for i in range(n_t, 0, -1):
                self.tridag(a, b, c, f, fm, n_s + 1)
                for j in range(1, n_s):
                    f[j] = fm[j]
        elif 'd' == bc and 'call' == self.stock.kind:  # Dirichlet Condition for call
            for i in range(n_t, 0, -1):
                self.tridag(a, b, c, f, fm, n_s + 1)
                for j in range(1, n_s):
                    f[j] = fm[j]
                f[n_s] = smax - k * math.exp(-r * (t - dt * i))
                f[0] = 0
        elif 'd' == bc and 'put' == self.stock.kind:  # Dirichlet Condition for call
            for i in range(n_t, 0, -1):
                self.tridag(a, b, c, f, fm, n_s + 1)
                for j in range(1, n_s):
                    f[j] = fm[j]
                f[n_s] = 0
                f[0] = k * math.exp(-r * (t - dt * i))
        elif 'm' == bc:  # my own solution
            for i in range(n_t, 0, -1):
                self.tridag(a, b, c, f, fm, n_s + 1)
                for j in range(1, n_s):
                    f[j] = fm[j]
                f[0] = f[0] * math.exp(r * dt)
                f[n_s] = f[n_s] * math.exp(r * dt)
        elif '' == bc:  # no discounting
            for i in range(n_t, 0, -1):
                self.tridag(a, b, c, f, fm, n_s + 1)
                for j in range(0, n_s + 1):
                    f[j] = fm[j]
                # print(f)

        else:
            return False

        return f[int(n_s / 2)]
