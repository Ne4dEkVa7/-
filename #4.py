#4.1
names = ['Богдан','Виолетта','Вадим']
for name in names:
    print(f'Здравствуй, {name}, хочу тебя пригласить на своё др в это воскресенье.')
#4.2
del names[2]
names.insert(2, 'Андрей')
for name in names:
    print(f'Здравствуй, {name}, хочу тебя пригласить на своё др в это воскресенье.')
#4.3
names.insert(0, 'Игорь')
names.insert(2, 'Никита')
names.append('Даша')
for name in names:
    print(f'Здравствуй, {name}, хочу тебя пригласить на своё др в это воскресенье.')
print(len(names))
#4.4
print(f'Я сожалею, {names[2]}, но др отменяется.')
names.pop(2)
print(f'Я сожалею, {names[2]}, но др отменяется.')
names.pop(2)
print(f'Я сожалею, {names[2]}, но др отменяется.')
names.pop(2)
print(f'Я сожалею, {names[2]}, но др отменяется.')
names.pop(2)
print(f'{names[0]}, др остаётся в силе')
print(f'{names[1]}, др остаётся в силе')
del names[0]
del names[0]
print(names)