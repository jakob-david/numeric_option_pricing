import math


def calcNS(n_t, Smax, vola, T):
    return int(math.log(Smax)/(vola*math.sqrt(3*(T/n_t))))