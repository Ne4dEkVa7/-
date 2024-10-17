#9.2
#1
dog = 89
cat = 98
if dog == cat:
    print('Строки равны')
else:
    print('Строки не равны')
dog = 96
cat = 96
if dog == cat:
    print('Строки равны')
else:
    print('Строки не равны') 
#2
mouse = ('Маленькая')
cat  = ('МАЛЕНЬКАЯ') 
if mouse.lower() == cat.lower():
    print('Строки равны')
else:
    print('Строки не равны')
mouse = ('Маленькая')
cat  = ('БОЛЬШАЯ') 
if mouse.lower() == cat.lower():
    print('Строки равны')
else:
    print('Строки не равны')
#3
chislo = int(input('Равно, больше, меньше: '))
vtoroe_chislo = int(input('Равно, больше, меньше: '))
if chislo == vtoroe_chislo:
    print('Числа равны')
elif chislo > vtoroe_chislo:
    print(f'{chislo} больше {vtoroe_chislo}')
elif chislo < vtoroe_chislo:
    print(f'{chislo} меньше {vtoroe_chislo}')
tretye_chislo = int(input('Больше или равно: '))
chetvyortoe_chislo = int(input('Больше или равно: '))
if tretye_chislo >= chetvyortoe_chislo:
    print('Yeeeeees')
else:
    print('NOOOO')
pyatoe_chislo = int(input('Меньше или равно: '))
shestoe_chislo = int(input('Меньше или равно: '))
if pyatoe_chislo <= shestoe_chislo:
    print('Yeeeeees')
else:
    print('NOOOO')
#4 Свет в общаге
sergey = input('Включить свет? ')
denis = input('Включить свет? ')
nikita = input('Включить свет? ')
if sergey.lower() and denis.lower() and nikita.lower() == 'да':
    print('Включить свет')
elif sergey.lower() or denis.lower() or nikita.lower() == 'нет':
    print('Не включать свет')
elif sergey.lower() and denis.lower() and nikita.lower() == 'нет':
    print('Не включать свет')
#5
fruits = ['банан','ананас','яблоко','персик']
fruit = input('Фрукт: ')
if fruit in fruits:
    print(f'Я люблю {fruit}.')
elif fruit not in fruits:
    print(f'Я не люблю {fruit}.')
