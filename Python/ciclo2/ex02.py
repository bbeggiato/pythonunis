#Python 3.10.8
import math
while True:
    try:
        a = int(input('Digite o valor do lado "A": '))
        b = int(input('Digite o valor do lado "B": '))
        c = int(input('Digite o valor do lado "C": '))
        if a <= 0 or b <= 0 or c <= 0:
            print('--'*19)
            print('Favor digitar apenas valores positivos')
            print('--'*19)
        else:
            break
    except ValueError:
        print('Você não digitou um número!')

if a > (b+c) or b > (a+c) or c > (a+b):
    print(f'Os valores de a: {a}, b: {b} e c: {c} não formam um Triângulo')
else:
    p = (a+b+c)/2 # Calculo do Perimetro
    area = math.sqrt(p*(p-a)*(p-b)*(p-c)) # Com o Perímetro calculo a área
    print('--' * 14)
    print(f'A \033[36mÁrea\033[m do triângulo é:\033[33m {area:.2f}\033[m')
    print('--' * 14)

    

















