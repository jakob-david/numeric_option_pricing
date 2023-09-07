def tridag(a, b, c, r, u, n):

    # Solves for a vector u[1..n] the tridiagonal linear set given by equation (2.4.1). a[1..n],
    # b[1..n], c[1..n], and r[1..n] are input vectors and are not modified.

    j = 0
    bet = 0
    gam = [0] * n

    if b[0] == 0.0:
        return False

    bet = b[0]
    u[0] = r[0] / (bet)

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
