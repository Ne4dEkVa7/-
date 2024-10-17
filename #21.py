#21.1
def sandwich(*toppings):
    print('Ваш  сэндвич будет сделан с: ')
    for topping in toppings:
        print(f'-{topping}')
sandwich('Колбаса','Капуста','Сыр')
sandwich('Колбаса','Капуста')
sandwich('Колбаса')
#21.2
name = input('Введите имя: ')
fam = input('Введите фамилию: ')
age = input('Введите свой возраст: ')
adress = input('Введите свой адрес: ')
klass = input('Введите свой класс: ')
def build_profile(names,fams,ages,adresses,klasses):
    print(f'Ваш профиль создан: {names}, {fams}, {ages}, {adresses},{klasses}')
build_profile(name,fam,age,adress,klass)  
#21.3
def cars(mark,model,**carinf):
    information = {'mark':mark,'model':model}
    information.update(carinf)
    return information
car = cars('Mazda','Rx5',color='blue',HP=453)
print(car)  