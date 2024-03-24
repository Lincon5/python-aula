"""manupulação de texto"""

"""Fatiamento"""
# frase[algum número dentro]
# frase[9:13] começa do 9 até o 12
# Exemplo:
"""frase = 'Curso em Video Python'
   print(frase[9:12])
   Resultado: VID"""

# frase[9:21:2] com : ele vai pulando de duas em duas casa.
# Exemplo:
"""frase = 'Curso em Video Python'
print(frase[9:21:2])
Resultado: VdoPto"""

# frase[:5] colocando : no incio, ele vai começar da casa 0.
# Exemplo:
"""frase = 'Curso em Video Python'
print(frase[:5])
Resultado: Curso"""

# frase [9::3] com um número e :: e um número no final ele começa do número indicado e pulando a quantidade do número que vc colocar no final
# Exemplo:
"""frase = 'Curso em Video Python'
print(frase[9::3])
Resultado: VePh"""


"""Análise"""
# função LEN(frase) significar comprimento, vai mostra o comprimento da frase.
# Exemplo:
"""frase = 'Curso em Video Python'
print(len(frase))
Resultado: 21 caractere"""

# função frase.count() para contar o que esta escrito  dentro to parentes, ex: 'Letra o' quantas vezes aparece.
# Exemplo:
"""frase = 'Curso em Video Python'
print(frase.count('o'))
Resultado: 3"""

# função frase.find('alguma coisa') find e encontrar, essa função vai encontar algo que esta escrito entre parentes.
# Exemplo:
"""frase = 'Curso em Video Python'
print(frase.find('Python'))
Resultado: 15, por que  ele vai indicar aonde começa a palavra Python."""

# função 'curso' in frase, tem a palavra que esta entre as aspas  na frase.
# Exemplo:
"""frase = 'Curso em Video Python'
print('Curso' in frase)
Resultado: TRUE, por que ele achou."""

"""Transformação"""
# funçaõ frase.replace('Pyton', 'Android'), replace significa trocar ele vai trocar as palavras.
# Exemplo:
"""frase = 'Curso em Video Python'
print(frase.replace('Python', 'Java'))
Resultado: Curso em Video Java, fez a troca de palavra."""

# função frase.upper(), upper significa pra cima, ele vai colocar todas as letras em maiúsculo.
# EXEMPLO:
"""frase = 'Curso em Video Python'
print(frase.upper())
Reseultado: CURSO EM VIDEO PYTHON."""

# função frase.lower(), coloca em minúscula.
# Exemplo:
"""frase = 'Curso em Video Python'
print(frase.lower())
Resultado: curso em video python"""

# função frase.capitalize(), ele vai deixar só a primeira letra em maiúscula, o resta fica em minúscula.
# Exemplo:
"""frase = 'Curso em Video Python'
print(frase.capitalize())
Resultado: Curso em video python"""

# função frase.title(), ele vai deixar as iniciais de cada palavra com espaço em maiúscula.
# Exemplo:
"""frase = 'Curso em Video Python'
print(frase.title())
Resultado: Curso Em Video Python"""

# função frase.strip(), ele vai remover todos os epaços inuteis no inicio é no final.
# Exemplo:
"""frase = str(input('digite algo:'))
print(frase.strip())"""

# função frase.rstrip(), vai remover só os espaços da direita final.
# Exemplo:
"""frase = str(input('digite algo:'))
print(frase.rstrip())"""

# função frase.lstrip(), vai remover os espaços da esquerda inicio.
# Exemplo:
"""frase = str(input('digite algo:'))
print(frase.lstrip())"""

"""Divisão"""
# função frase.split(), vai criar uma divisão onde tem espaço. vai dividir uma string em lista.
# Exemplo:
"""frase = str(input('digite algo:'))
print(frase.split())
Resultado: ['Lincon', 'da', 'Silva', 'Souza']"""

"""Junção"""
# função '-'.join(frase), join é para juntar as palavras
# Exemplo:
"""frase = str(input('digite algo:'))
print('-'.join(frase))
Resultado: l-i- -c-o"""

frase = 'Curso em Video Python'
print(frase.upper())
print(len(frase))
