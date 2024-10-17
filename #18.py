#18.1
def favorite_book(title):
    print(f'My favorite books is {title}')
favorite_book('Alice in Wonderlands')
#18.2.1
def make_shirt(rzm, txt):
    print(rzm)
    print(txt)
make_shirt(input('Введите размер: '),input('Введите текст на принт: '))
#18.2.2
def make_shirt(rzm, txt):
    print(rzm)
    print(txt)
make_shirt(txt=input('Введите текст на принт: '),rzm=input('Введите размер: '),)
#18.3
rzm = 'L'
txt = 'Я люблю питон'
choose=input('Изменить размер? ')
if choose.lower() == 'да':
    def make_shirt(rzm,txt):
        print(rzm)
        print(txt)
    make_shirt(input('Введите размер: '),input('Введите текст на принт: '))
else:
    make_shirt(rzm,txt)  
#18.4
cities = {'Тюмень':'России','Москва':'России'}
choose=input('Ваш город это Тюмень или Москва? ')
if choose.lower() == 'нет':
    def describe_city(city,country):
        print(f'{city} находится в {country}.')
    describe_city(input('Введите ваш город: '),input('Введите вашу страну: '))
else:
    for city in cities:
        print(f'{city} находится в {cities[city]}')
#18.5
def carsell(car):
    print(f'Хорошо, мы предоставим вам {car}')
carsell(input('Какую машину вы бы хотели арендовать? '))