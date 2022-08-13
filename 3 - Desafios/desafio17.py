import math
catetoOposto = float(input('Digite o cateto oposto deste triângulo: '))
catetoAdjacente = float(input('Digite o cateto adjacente deste triângulo: '))
hipotenusa = math.hypot(catetoOposto, catetoAdjacente)
print('A hipotenusa do cateto oposto {} e o cateto adjacente {} é igual a: {:.2f}'.format(catetoOposto, catetoAdjacente, hipotenusa))
