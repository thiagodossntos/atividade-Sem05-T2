def letra(palavras):
    if palavras in 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ':
        return True
    else:
        return False

palavras = input()
if letra(palavras):
    print(True)

else:
    print(False)

