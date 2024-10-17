#20.2.5
#1
name = input('Введите своё имя: ')
age = int(input('Введите свой возраст: '))
print(f'Привет, {name}! Тебе {age} лет)')
#2
cities = ['Тюмень','Москва','Новосибирск','Астрахань','Пермь']
print(f'Города: ',', '.join(cities))
#3
chislo = int(input('Введите число: '))
if chislo %2 == 0:
    print(chislo , 'является чётным числом')
else:
    print(chislo , 'является нечётным числлом.')
#4
def sum(x,y):
    z=x+y
    return z
x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
print(sum(x,y))
#5
fruits={'Банан':'230руб/кг','Ананас':'400руб/кг','Яблоки':'100руб/кг'}
for fruit in fruits:
    print(f'{fruit} Цена: {fruits[fruit]}')
#6
for number in range(1,10):
    print(number **2)
#7
while 1:
    x=int(input('Введите число: '))
    print(x)
    if x == 0:
        break
#8
empty = []
while len(empty)!=5:
    fut = int(input('Введие число для добавления в список: '))
    empty.append(fut)
y = sum(empty,0)/len(empty)
print(y)
#9
fruits = {'Банан':'230руб/кг','Ананас':'400руб/кг','Яблоки':'100руб/кг'}
fruit = input('Введите название нужного фрукта: ')
if fruit.capitalize() in fruits:
    print(f'{fruit.capitalize()} продаётся по цене {fruits[fruit.capitalize()]}')
else:
    print(f'У нас не продаётся {fruit.capitalize()}')
#10
import random
count = 5
minz = -100
maxz = 100
empty = [random.randint(minz,maxz) for _ in range(count)]
print(empty)
print(sorted(empty))
#11
