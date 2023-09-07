import math


class FiniteDifference:

    def get_parameters_form_stock(self, stock):
        s = stock.S
        k = stock.K
        t = stock.T
        r = stock.r
        q = stock.d
        sigma = stock.v

        return s, k, t, r, q, sigma

    def get_parameters(self, n_s, n_t, s, t, sigma):

        smax = 2 * s

        if n_s:
            n_s = self.calcNS(n_t, smax, sigma, t)
            n_s = n_s + (n_s % 2)
        else:
            n_s = n_s + (n_s % 2)

        n_s = int(n_s)

        dt = t / n_t
        ds = 2 * s / n_s

        return smax, n_s, dt, ds

    def get_arrays(self, size, number):

        ret = list()
        for i in range(0, number):
            ret.append([0] * (size + 1))

        return tuple(ret)

    def get_f_array(self, size, ds, k, kind):

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

    def calcNS(self, n_t, Smax, vola, T):
        return int(math.log(Smax) / (vola * math.sqrt(3 * (T / n_t))))

    def tridag(self, a, b, c, r, u, n):

        # Solves for a vector u[1..n] the tridiagonal linear set given by equation (2.4.1). a[1..n],
        # b[1..n], c[1..n], and r[1..n] are input vectors and are not modified.

        j = 0
        bet = 0
        gam = [0] * n

        if b[0] == 0.0:
            return False

        bet = b[0]
        u[0] = r[0] / bet

        j = 1
        for j in range(1, n):
            gam[j] = c[j - 1] / bet
            bet = b[j] - a[j] * gam[j]

            if bet == 0.0:
                return False

            u[j] = (r[j] - a[j] * u[j - 1]) / bet

        for j in range(n - 2, 0, -1):
            u[j] -= gam[j + 1] * u[j + 1]

        return u
