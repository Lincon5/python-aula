#Estrutura de repetição while.

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('quer continuar? [S/N] ' )).upper()
print('Fim')'''

'''par = 0
impar = 0
n = 1
while n != 0:
    n = int(input('Digite um valor:'))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))'''

senha = input("Digite uma senha: ")

while senha != "1234":
    print("Senha incorreta!")
    senha = input("Digite uma senha: ")

print("Senha correta! Acesso permitido.")

#O comando while faz com que um conjunto de instruções seja executado enquanto uma condição é atendida. Quando o resultado dessa condição passa a ser falso, a execução do loop é interrompida