def nty_wyraz(a1, q, n):
    return a1 * pow(q, (n - 1))
def suma_n_wyrazow(a1, q, n):
    if q != 0:
        return a1 * ((1 - pow(q, n)) / (1 - q))
    if q == 0:
        return a1 * q