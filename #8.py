#8.1
forest = ['Ягоды','Грибы','Деревья','Мох','Животные']
print(f'The irst three items in the list: {forest [:3]}')
print(f'The irst three items in the list: {forest [1:4]}')
print(f'The irst three items in the list: {forest [2:]}')
#8.2
pizzas = ['Пеперони','Гавайская','Салями']
friends_pizzas = ['Пеперони','Гавайская','Салями']
pizzas.insert(0,'Мацарелла')
friends_pizzas.insert(3,'4 сыра')
for pizza in pizzas:
    print(f'Моя любимая пицца это: {pizza}')
for pizza in friends_pizzas:
    print(f'Любимая пицца моих друзей это: {pizza}')
#8.3
foods = ('Борщ','Окрошка','Чай','Кофе','Хлеб')
for food in foods:
    print(f'{food}')
foods.remove('Хлеб')
foods = ['Борщ','Окрошка','Чай','Кофе','Хлеб']
foods.remove('Борщ')
foods.insert(0,'Солянка')
foods.remove('Кофе')
foods.insert(3,'Компот')
for food in foods:
    print(f'{food}')