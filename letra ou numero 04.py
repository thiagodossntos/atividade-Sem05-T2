def letra(palavras):
    if palavras in 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789':
        return True
    else:
        return False

palavras = input()
if letra(palavras):
    print(True)

else:
    print(False)
