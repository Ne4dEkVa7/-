#17.1
sandwich_orders = ['гамбургер','дэгвуд','субмарина','Сырный']
finished_sandwich = []
for sd in sandwich_orders:
    print(f"Я сделаю твой {sd.title()}")
    finished_sandwich.insert(0, sd.title())
sandwich_orders.clear()
print(f'Готовые сендвичи: {finished_sandwich}')
print(sandwich_orders)
#17.2
sandwich_orders = ['гамбургер','С сыром','дэгвуд','С сыром','субмарина','Без сыра','С сыром']
while 'С сыром' in sandwich_orders:
       sandwich_orders.remove('С сыром')
print(sandwich_orders)
#17.3
otps = {}
while 1:
    name = input('Введите имя ')
    otp = input('Где вы проведёте отпуск? ')
    pvt = input('Сколько вы проведёте в этом месте? ')
    otps[name] = otp
    pvt = input("Вернуться на главную страницу? ")
    if pvt.title() == 'Да':
        break
    for name,otp in otps.items():
        print(f"{name} хочет провести отпуск в {otp}")
print('Опрос завершён')