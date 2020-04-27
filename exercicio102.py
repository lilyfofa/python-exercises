def fatorial(n, show=False):
    """
    -> Calcula o fatorial do número solicitado.
    :param n: o valor que será utilizado no cálculo (n!)
    :param show: define se o cálcuo será mostrado
    :return: a resposta do fatorial
    """
    factorial = 1
    while n > 0:
        if show:
            print(f'{n} '+'x ' if n > 1 else f'{n} = ', end='')
        factorial *= n
        n -= 1
    print(factorial)
    return factorial


fatorial(int(input('Digite um número para ver seu fatorial: ')), show=False)
help(fatorial.__doc__)