class Stock:

    def __init__(self):
        """
        A class which holds all relevant parameters of a stock.
        """

        self.s = 42  # spot price
        self.k = 40  # strike price
        self.t = 1  # time
        self.r = 0.1  # risc free interest rate
        self.d = 0  # dividend
        self.v = 0.2  # volatility
        self.kind = 'call'  # type of the Option (call or put)

        self.fdm_factor = 25

    def set_option(self, s, k, t, r, d, v, kind):
        """
        Resets almost all parameters of the class.

        :param s: spot price
        :param k: strike price
        :param t: time
        :param r: risc free interest rat
        :param d: dividend
        :param v: volatility
        :param kind: type of the Option (call or put)
        """

        self.s = s
        self.k = k
        self.t = t
        self.r = r
        self.d = d
        self.v = v
        self.kind = kind

    def set_fdm_factor(self, fdm_factor):
        """
        Sets the Fdm Factor for the stock.

        :param fdm_factor: The new Fdm Factor.
        """

        self.fdm_factor = fdm_factor

    def set_kind(self, kind):
        """
        Sets the kind of the stock.

        :param kind: The new kind.
        """

        self.kind = kind

    def set_stock(self, s):
        """
        Sets the spot price of the stock.

        :param s: The new spot price.
        """

        self.s = s

    def __str__(self):
        """
        Returns a string with all parameters of the stock.

        :return: string with all parameters of the stock.
        """

        msg = "spot price:\t\t{s}\n".format(s=self.s)
        msg += "strike price:\t{k}\n".format(k=self.k)
        msg += "time:\t\t\t{t}\n".format(t=self.t)
        msg += "risk free interest rate: {r}\n".format(r=self.r)
        msg += "dividend:\t\t{d}\n".format(d=self.d)
        msg += "volatility:\t\t{v}\n".format(v=self.v)
        msg += "kind:\t\t\t{kind}\n".format(kind=self.kind)

        return msg
