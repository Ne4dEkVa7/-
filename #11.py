#11.1
users = ['Максим','Давид','Вася','Коля','Admin']
for user in users:
    if user == 'Admin':
        print(f'Hello, {user}, would you like to see a status report?')
    else:
        print(f'Hello, {user}, thank you for logging in again')
#11.2    
current_users = ['Максим','Петя','Коля','Вася','Богдан']
new_users = ['Петя','Арсений','Эдик','Максим','Артём']
for name in new_users:
    if name in current_users:
        print('Пожалуйста, выберите новое имя.')
    else:
        print('Данное имя доступно для регистрации.')    
#11.3
numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')