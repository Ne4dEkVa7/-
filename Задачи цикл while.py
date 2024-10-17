#1 Остаток
a=int(input('Введите число A: '))
b=int(input(f'Введите число меньше {a} : '))
while 1:
    if a<b:
        print(f'Оcтаток: {a}')
        break
    else:
       a=a-b
#2 Дюймы
dm=2.54
sm=10
while 1:
    if sm<=20:
        dms=sm*dm
        print(f'{sm}см = {dms}')
        sm=sm+1
    else:
        break
#3 Нули
kolvo=int(input("Сколько раз написать 'ноль'? "))
num=kolvo
while 1:
    if num!=0:
        print('Ноль')
        num=num-1
    else:
      break
#4 Квадраты
kvadrat=400
while 1:
    if kvadrat ==0:
        break
    else:
        print(f"{kvadrat} - {kvadrat**2}")
        kvadrat=kvadrat-8