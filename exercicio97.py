def título(msg):
    espaco = len(msg)
    print('-' * (espaco + 10))
    print(' '*5 + msg + ' ' * 5)
    print('-' * (espaco + 10))


título(str(input('Digite a mensagem: ')))
