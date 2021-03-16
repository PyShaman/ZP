a = input('Podaj liczbe: ')
b = []
for _ in a:
    b.append(_)
b.reverse()
for _ in b:
    print(f'{_} ', end='')
