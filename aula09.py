"""manupulação de texto"""
"""Fatiamento"""
# frase[algum número dentro]
# frase[9:13] começa do 9 até o 12
# frase[9:21:2] com : ele vai pulando de duas em duas casa.
# frase[:5] colocando : no incio, ele vai começar da casa 0.
# frase[9::3] com um número e :: e um número no final ele começa do número indicado e pulando a quantidade do número que vc colocar no final

"""Análise"""
# função LEN(frase) significar comprimento, vai mostra o comprimento da frase.
# função frase.count() para contar o que esta escrito  dentro to parentes.
# função frase.find('alguma coisa') find e encontrar, essa função vai encontar algo que esta escrito entre parentes.
# função 'curso' in frase, tem a palavra que esta entre as aspas  na frase.

"""Transformação"""
# funçaõ frase.replace('Pyton', 'Android'), replace significa trocar ele vai trocar as palavras.
# função frase.upper(), upper significa pra cima, ele vai colocar todas as letras em maiúsculo.
# função frase.lower(), coloca em minúscula.
# função frase.capitalize(), ele vai deixar só a primeira letra em maiúscula, o resta fica em minúscula.
# função frase,title(), ele vai deixar as iniciais de cada palavra com espaço em maiúscula.
# função frase.strip(), ele vai remover todos os epaços inuteis no inicio é no final.
# função frase.rstrip(), vai remover só os espaços da direita final.
# função frase.lstrip(), vai remover os espaços da esquerda inicio.

"""Divisão"""
# função frase.split(), vai criar uma divisão onde tem espaço. vai dividir uma string em lista.

"""Junção"""
# função '-'.join(frase), join é para juntar as palavras

frase = 'Curso em Video Python'
print(frase.upper())
print(len(frase))

