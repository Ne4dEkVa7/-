#14.1
zinovyev = {'first_name':'Arseniyi','last_name':'Zinovyev','age':17,'city':'Tyumen'}
efimov = {'first_name':'Vadim','last_name':'Efimov','age':18,'city':'Tyumen'}
vigovvskiyi = {'first_name':'Bogdan','last_name':'vigovvskiyi','age':18,'city':'Tyumen'}
peoples = [zinovyev,efimov,vigovvskiyi]
for people in peoples:
    print(f"{people['first_name']} {people['last_name']} {people['age']} {people['city']}")
#14.2
Максим = '228;144;256'
Арсений = '666;444;555'
Рим = '69;96'
Фархат = '6;5;4;3;2;1'
Вадим = '52;25;72;27'
chisla = {'Максим':Максим,'Арсений':Арсений,'Рим':Рим,'Фархат':Фархат,'Вадим':Вадим}
for name in chisla:
    print(f"{name} : {chisla[name]}")
#14.3
fact1= 'Тюмень является первым русским городом в сибири.'
fact2=  'Во времена СССР являлся столицей двух республик: Ингушской и Северо-Осетинскойю'
fact3= 'В Голливуде находится много киностудий и живут многие известные киноактёры.'
g1 = {'country':'Россия','population':'Население: 860k','fact': fact1}
g2 = {'country':'Россия','population':'Население: 290k','fact': fact2}
g3 = {'country':'США','population':'Население: 210k','fact': fact3}
cities = {'Тюмень':g1,'Владикавказ':g2,'Голливуд':g3}
for city in cities:
    if city.lower() == 'тюмень':
        print(f'{city}: {g1["country"]}, {g1["population"]}, {g1["fact"]}')
    elif city.lower() == 'владикавказ':
        print(f'{city}: {g2["country"]}, {g2["population"]}, {g2["fact"]}')
    elif city.lower() == 'голливуд':
        print(f'{city}: {g3["country"]}, {g3["population"]}, {g3["fact"]}')    