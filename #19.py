#19.1
def city_country(city,country):
    return f"'{city}, {country}'"
city=input('Введите город: ')
country=input('Введите страну: ')
print(city_country(city.title(),country.title()))
#19.2
def make_album(artist,opisanie):
    return {f'Исполнитель':artist,'Название':opisanie}
album1=make_album('Skillet','Comatose')
album2=make_album('ATL','Радио Апокалипсис')
album3=make_album('2rbina2rista','Астралопитек')
print(album1)
print(album2)
print(album3)
#19.3
def make_album(artist,opisanie,kolvo): 
    if kolvo:
        full = {'Исполнитель': artist, 'Альбом': opisanie, 'Количество треков':kolvo}
    else:
        full = {'Исполнитель': artist, 'Альбом': opisanie}    
    return full
album1=make_album('Skillet','Comatose','')
album2=make_album('ATL','Радио Апокалипсис','')
album3=make_album('2rbina2rista','Астралопитек','9')
print(album1)
print(album2)
print(album3)
#19.4
while 1:
    start = input('Хотите добавить альбом в список? ')
    if start.lower() == 'да':
        def make_album(artist,album,kolvo):
            if kolvo:
                full={f'Исполнитель': artist,'Альбом': album,'Количество треков' : kolvo}
                return f"{full['Исполнитель']},{full['Альбом']},{full['Количество треков']}"
            else:
                full={f'Исполнитель': artist,'Альбом':album}
                return f"{full['Исполнитель']},{full['Альбом']}"     
        albums=make_album(input('Введите артиста: '), input('Введите название альбома: '),input('Введите количество треков в альбоме: '))
        print(albums)               
    else:
        print('Программа заверщена.')
        break
#19.5
message1 = 'Это первое сообщение'
message2 = 'А это второе сообщение'
message3 = 'Ну и третье сообщение'
def show_message(message):
    return message
messages = [message1,message2,message3]
for message in messages:
    print(show_message(message))