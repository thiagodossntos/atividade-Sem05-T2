def letra(palavras):
    if palavras in 'AEIOUaeiou':
        return True
    else:
        return False

palavras = input('digite uma vogal: ')
if letra(palavras):
    print(True)

else:
    print(False)
