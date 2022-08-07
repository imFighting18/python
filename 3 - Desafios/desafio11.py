largura = float(input('Digite a largura da parede (em M): '))
altura = float(input('Digite a altura da parede (em M): '))
area = largura * altura
litros = area / 2
print("A área desta parede é: {:.3f}\nÉ preciso de {:.4f}L de tinta para pintar esta parede!".format(area, litros))
