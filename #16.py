#16.1
pizza='Добавить добавки в пиццу? '
pizza+="\nВы можете выйти набрав 'Выход'"
topping=''
while topping.title() != 'Выход':
    topping=input(pizza)
    print(f'{topping} добавлено в ваш заказ.')
print('Добавление закончено')
#16.2
price={'baby':'бесплатный','12':'10$','12+':'15$'}
age=int(input('Введите свой возраст: '))
if age<3:
    print(f"Билет {price['baby']}, приятного просмотра!")
elif 3<=age<=12:
    print(f"Цена: {price['12']}, приятного просмотра!")
elif 13<=age:
    print(f"Цена: {price['12+']}, приятного просмотра!")
#16.3.1
active=1
pizza='Добавить добавки в пиццу? '
pizza+="\nВы можете выйти набрав'Выход'"
topping=''
while active:
    topping=input(pizza)
    if topping.title() == 'Выход':
        active = 0
    else:
        print(f"{topping.title()} добавлено.")
print('Добавление закончено')
#16.3.2
pizza='Добавить добавки в пиццу? '
pizza+="\nВы можете выйти набрав'Выход'"
topping=''
while 1:
    topping=input(pizza)
    if topping.title() == 'Выход':
        break
    else:
        print(f"{topping.title()} добавлено.")
print('Добавление закончено')