# Condições Alinhadas.( Usando o ELIF)

nome = str(input('Qual é seu nome?')).title()
if nome == 'Lincon':
    print('Seja Bem vindo {}, você tem acesso a todos andares.'.format(nome))
elif nome == 'Ana' or nome == 'Pedro' or nome == 'Lucas':
    print('\033[0;31mNão tem acesso a essa area.\033[m')
elif nome in 'Rodrigo Alan Luffy Carla':
    print('Você tem acesso ao \033[0;36m1°,2°,3°\033[m e \033[0;36m4°\033[m andar.')
else:
    print("Nome não reconhecido.")
