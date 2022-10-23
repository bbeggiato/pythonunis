import math
while True:
    try:
        a = int(input('Digite o valor do lado "A": '))
        if a <= 0:
            print('--'*19)
            print('Favor digitar apenas valores positivos')
            print('--'*19)
            break
    except ValueError:
        print('Você não digitou um número!')
    try:
        b = int(input('Digite o valor do lado "B": '))
        if b <= 0:
            print('--'*19)
            print('Favor digitar apenas valores positivos')
            print('--'*19)
    except ValueError:
        print('Você não digitou um número!')
    try:
        c = int(input('Digite o valor do lado "C": '))
        if c <= 0:
            print('--'*19)
            print('Favor digitar apenas valores positivos')
            print('--'*19)
        else:
            break
    except ValueError:
        print('Você não digitou um número!')

    print('Você não digitou um número!')

if a > (b+c) or b > (a+c) or c > (a+b):
    print(f'Os valores de a: {a}, b: {b} e c: {c} não formam um Triângulo')
else:
    p = (a+b+c)/2 # Calculo do Perimetro
    area = math.sqrt(p*(p-a)*(p-b)*(p-c)) # Com o Perímetro calculo a área
    print(f'A área do triângulo é: {area:.2f}')

