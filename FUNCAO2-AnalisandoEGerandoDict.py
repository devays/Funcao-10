def notas(*num, sit = False):
    aluno = dict()
    soma = 0
    for c in range(0,len(num)):
        soma = soma + num[c]
    media = soma / len(num)
    if sit == True:
        if media < 6: 
            aluno = {'total': len(num), 'maior': max(num), 'menor': min(num), 'media': media, 'situação': 'RUIM'}
        else:
            aluno = {'total': len(num), 'maior': max(num), 'menor': min(num), 'media': media, 'situação': 'BOA'}
    else:
        aluno = {'total': len(num), 'maior': max(num), 'menor': min(num), 'media': media}
    print(aluno)



notas(10,10,10, sit=True)


