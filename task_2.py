first = int(input('Введите первое число прогрессии: '))
znamenatel = int(input('Введите знаменатель прогрессии: '))
colvo = int(input('Введите количество чисел в прогрессии: '))

for i in range(colvo):
    print(first, end=' ')
    first = first * znamenatel