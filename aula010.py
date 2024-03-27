# aula de Condições simples e compostas.

# carro.siga().
# carro e nosso objeto
# siga() e nosso metado, metado sempre tem parentes no final.

"""Condição simples."""
# Usei o .title(), no código caso o usuário escreva o nome com lerta maiúscula.
#nome = str(input('Qual seu nome?')).title()
#if nome == 'Lincon':
 #   print('belo nome você tem!')
#print('Boa noite, {}'.format(nome))

"""Condição composta."""
n1 = float(input('Digite uma nota:'))
n2 = float(input('Digite uma nota:'))
n3 = float(input('Digite uma nota:'))
n4 = float(input('Digite uma nota:'))
m = (n1 + n2 + n3 + n4)/4
print('A sua média foi {:.1f}'.format(m))
if m >= 5.0:
    print('Aprovado, parabéns.')
else:
    print('Reprovado, estude mais próximo ano.')