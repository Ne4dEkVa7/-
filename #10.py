#10.1
color = ["Red","Yellow","Green"]
if color[0] == "Red":
    print(f'The traffic light is {color[0]}')
if color[1] == "Yellow":
    print(f'The traffic light is {color[1]}')
if color[2] == "Green":
    print(f'The traffic light is {color[2]}')    
#10.2
age = 27
if age < 2:
    print("Младенец")
elif 2 <= age <= 4:
    print("Малыш")
elif 4 <= age <= 13:
    print("Ребёнок")
elif 13 <= age <= 20:
    print("Подросток")
elif 20 <= age <= 65:
    print("Взрослый")
else:
    print("Пожилой")   
#10.3
favorite_fruits = ["Bananas","Apple","Orange"] 
if "Bananas" in favorite_fruits:
    print('I like bananas.')    
if "Pineapple" not in favorite_fruits:
    print("I don't like pineapple") 
if "Apple" in favorite_fruits:
    print('I like apple.') 
if "Orange" in favorite_fruits:
    print('I like orange.') 
if "lemon" not in favorite_fruits:
    print("I don't like lemon.")    