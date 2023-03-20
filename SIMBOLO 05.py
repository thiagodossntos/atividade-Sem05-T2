def caractere(simbolo):
    if simbolo in '-/?;:.>,<]]}}{{ll':
        return True
    else:
        return False

simbolo = input('digite um simbolo qualquer: ')
if caractere(simbolo):
    print(True)

else:
    print(False)

