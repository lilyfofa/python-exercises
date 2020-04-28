def notas(* n, sit=False):
    """
    -> Ferramenta de análise de notas.
    :param n: as notas dos alunos
    :param sit: mostra a situação da turma quanto à média.
    :return: um dicionário com estatísticas sobre as notas enviadas.
    """
    media = sum(n) / len(n)
    turma = dict()
    turma['Quantidade'] = len(n)
    turma['Maior nota'] = max(n)
    turma['Menor nota'] = min(n)
    turma['Média'] = f'{sum(n) / len(n):.2f}'
    if sit:
        if media < 6:
            turma['Situação'] = 'Ruim'
        elif 6 <= media < 7:
            turma['Situação'] = 'Razoável'
        else:
            turma['Situação'] = 'Ótima'
    return turma


print(notas(10, 5, sit=True))
print(help(notas))