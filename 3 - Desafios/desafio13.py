salario = float(input('Digite o salário do funcionário: '))
novosalario = (salario * 15/100) + salario
print('O novo salário do funcionário é: R${:.2f}'.format(novosalario))
