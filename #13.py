#13.2
rivers = {'Niel':'Egypt','Amazon':'Brazil','Mississipi':'USA','Yangtze':'China','Oby':'Russia'}
for river in rivers:
    print(f"{river}")
for river in rivers:
    print(f"{rivers[river]}")
for river in rivers:
    print(f"The {river} runs through {rivers[river]}")
#13.3
favorite_languages = {'Keit':'none','Jen':'Python','Eric':'none','Sarah':'C','Edward':'none'}
for language in favorite_languages.values():
    if language == 'none':
        print(f'Dear user, you can take a survey in our office.')
    else:
        print('Thank you for participating in the survey!')
#13.4
hobbies = {'Катя':'вязание','Маша':'рисование','Максим':'футбол','Марина':'футбол','Захар':'рисование'}
for hobbie in set(hobbies.values()):
    print(hobbie.title())
#13.5
users = {'user_1':'Biba','user_2':'Aboba','user_3':'Boba'}
print(users.keys())
user=input('Введите ключ: ')
if user in users:
    print(f"Ключ: {user}, значение: {users[user]}.")
    choose = input('Изменить значение ключа? ')
    if choose.lower() == 'да':
        new_key=input('Введите значение нового ключа: ')
        key={user:new_key}
        users.update(key)
        print(f'Ключ пользователя {user} изменён на: {new_key}')
        print(users)
    else:
        print('Ключ не будет изменён.')
else:
    print('Данного пользователя нет в списке.')