def letra(palavras):
    if palavras in 'bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXyYzZ':
        return True
    else:
        return False

palavras = input('digite um numero de 0 a 9 ou uma consoante, se nao vai aparecer false: ')
if letra(palavras):
    print(True)

else:
    print(False)

