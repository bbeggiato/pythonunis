
while True:
    lista = []

    try:
        Valor1 = int(input('Digite o Primeiro valor:'))
        Valor2 = int(input('Digite o Segundo valor:'))
        Valor3 = int(input('Digite o Terceiro valor:'))

    except ValueError:
        print('Favor digitar apenas valores numéricos')

    else:
        break

lista.append(Valor1)
lista.append(Valor2)
lista.append(Valor3)
print()
print(f'Você Digitou os Valores {lista}')
menor = min(lista)
print('--'*18)
print(f'\033[36mO Menor Valor entre os três é:\033[m \033[33m {menor}\033[m')
print('--'*18)
4
5
6
7




