# Estrutura de repetição for.
# FOR= laço
# C= Variavel que você pode escolher qual vai ser.
# IN= NO
# RANGE= Intervalo

#for c in range(1, 6): # nesse código de 1, 6, ele vai contar de 1 até 5.Por que no sexto número ele para, se quiser que ele conte até o 6 sempre coloca o próximo número.
#    print(c)
#print('Acabou')

#for c in range(6, 0, -1): # Para contar em ordem decrescemte temos que colocar -1 no final.
#   print(c)
#print('Acabou')

#for c in range(0, 7, 2): # O último número sempre vai ser a função do seu código, aqui ele leu de 0 a 7, pulando em 2 em 2.
#    print(c)
#print('Acabou')

# Outra maneira de fazer esse laço de repetição.

#n = int(input('Digite um número: ')) # mesmo principios que os códigos de cima.
#for c in range(0, n):
#    print(c)
#print('Acabou.')

#n = int(input('Digite um número: ')) # n+1 vai contar até o número que você escolheu.
#for c in range(0, n+1):
#    print(c)
#print('Acabou.')

#i = int(input('Início: ')) # o "i" vai ser o número inicial.
#f = int(input('Fim: '))    # o "f" vai ser onde ele para de contar, se quiser que ele conte até o número escolhido coloca f+1.
#p = int(input('Passo: '))  # o "p" vai ser o passo o número escolhido para ir pulando.
#for c in range(i, f+1, p):
#    print(c)
#print('Acabou.')

# Nessa situação a variavel n está dentro do laço, "for" então ele vai pedir-lhe digite 4 números.
#for c in range(0, 4):
#    n = int(input('Digite um número: '))
#print('Acabou.')

# usando  a estrutura for para fazer o calculo dos números.
s = 0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    s += n
print('A soma dos valores será de {}'.format(s))
