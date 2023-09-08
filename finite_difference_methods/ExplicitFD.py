import math

from finite_difference_methods.FiniteDifference import FiniteDifference


class ExplicitFD(FiniteDifference):

    def __init__(self, stock):
        """
        Solves the Black–Scholes equation using an explicit finite difference method.

        :param stock: The stock for witch the future price should be calculated. (class Stock)
        """

        self.stock = stock

    def calculate(self, n_s, n_t, bc):
        """
        Calculates the price using an explicit finite difference method.

        :param n_s: The number of starting prices.
        :param n_t: The number of time steps.
        :param bc:  The type of border conditions. (d...Dirichlet, n...von Neumann)

        :return: The price of the stock after t time.
        """

        s, k, t, r, q, sigma = self.get_parameters_form_stock(self.stock)
        smax, n_s, dt, ds = self.get_parameters(n_s, n_t, s, t, sigma)
        fm, a, b, c = self.get_arrays(n_s, 4)
        f = self.get_initial_array(n_s, ds, k, self.stock.kind)

        q = 0  # possible addition
        sigma_sq = sigma * sigma

        for j in range(0, n_s + 1):
            a[j] = 1 / (1 + r * dt) * (-.5 * (r - q) * j * dt + 0.5 * sigma_sq * j * j * dt)
            b[j] = 1 / (1 + r * dt) * (1 - sigma_sq * j * j * dt)
            c[j] = 1 / (1 + r * dt) * (.5 * (r - q) * j * dt + 0.5 * sigma_sq * j * j * dt)

            # a[j] = .5*j*dt*(j*sigma_sq-r)
            # b[j] = 1-dt*(j*j*sigma_sq +r)
            # c[j] = .5*j*dt*(j*sigma_sq+r)

        # von Neumann
        b[0] = b[0] + 2 * a[0]
        c[0] = c[0] - a[0]

        b[n_s] = b[n_s] + 2 * c[n_s]
        a[n_s] = a[n_s] - c[n_s]

        # the switch is not yet tested.

        if bc == 'n':  # von Neumann Condition
            for i in range(n_t, 0, -1):
                fm[0] = f[0] * b[0] + f[1] * c[0]
                fm[n_s] = f[n_s] * b[n_s] + f[n_s - 1] * a[n_s]
                for j in range(1, n_s):
                    fm[j] = a[j] * f[j - 1] + b[j] * f[j] + c[j] * f[j + 1]
                for j in range(0, n_s + 1):
                    f[j] = fm[j]

        elif 'd' == bc and 'call' == self.stock.kind:  # Dirichlet Condition for call
            for i in range(n_t, 0, -1):
                fm[n_s] = smax - k * math.exp(-r * (t - dt * i))
                fm[0] = 0
                for j in range(1, n_s):
                    fm[j] = a[j] * f[j - 1] + b[j] * f[j] + c[j] * f[j + 1]
                for j in range(0, n_s + 1):
                    f[j] = fm[j]

        elif 'd' == bc and 'put' == self.stock.kind:  # Dirichlet Condition for call
            for i in range(n_t, 0, -1):
                fm[n_s] = 0
                fm[0] = k * math.exp(-r * (t - dt * i))
                for j in range(1, n_s):
                    fm[j] = a[j] * f[j - 1] + b[j] * f[j] + c[j] * f[j + 1]
                for j in range(0, n_s + 1):
                    f[j] = fm[j]

        elif 'm' == bc:  # my own solution
            for i in range(n_t, 0, -1):
                fm[0] = f[0] * math.exp(r * dt)
                fm[n_s] = f[n_s] * math.exp(r * dt)
                for j in range(1, n_s):
                    fm[j] = a[j] * f[j - 1] + b[j] * f[j] + c[j] * f[j + 1]
                for j in range(0, n_s + 1):
                    f[j] = fm[j]

        elif '' == bc:  # no discounting
            for i in range(n_t, 0, -1):
                fm[0] = f[0]
                fm[n_s] = f[n_s]
                for j in range(1, n_s):
                    fm[j] = a[j] * f[j - 1] + b[j] * f[j] + c[j] * f[j + 1]
                for j in range(0, n_s + 1):
                    f[j] = fm[j]

        else:
            return False

        return f[int(n_s / 2)]