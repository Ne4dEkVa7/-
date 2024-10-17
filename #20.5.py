#20.5.1
def delenie(x,y):
    try:
        result = x/y
        print('Результат:', result)
    except ZeroDivisionError:
        print('Делить на ноль нельзя!)')
    finally:
        print('Спасибо)') 
x=12
y=0
delenie(x,y) 
#20.5.2
def chislo():
    try:
        userinput=input('Введите целое число: ')
        number=int(userinput)
        print(f'Вы ввели число: {number}')
    except ValueError:
        print('Вы ввели недопустимое число. Пожалуйста, введите целове число.')
chislo()
#20.5.3
print('Введите число:')
x=input()
print('Введите число:')
y=input()
try:
    z=x/y
    print(z)
except TypeError:
    z=int(x)/int(y)
    print(z)