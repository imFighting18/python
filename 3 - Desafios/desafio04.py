nome = input('Digite algo: ')
print('Tipo primitivo: {}'.format(type(nome)))
print('É Alpha Numeric? {}'.format(nome.isalnum()))
print('Está em letras maiúsculas? {}'.format(nome.isupper()))
print('É Alpha? {}'.format(nome.isalpha()))
print('Código ASCII? {}'.format(nome.isascii()))
print('É digito? {}'.format(nome.isdigit()))
print('Está em letras minúsculas? {}'.format(nome.islower()))
print('É um número? {}'.format(nome.isnumeric()))
