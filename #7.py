#7.1
for value in range(1,21):
    print(value)
#7.2
for value in range(1,1001):
    print(value)
#7.3
digits = list(range(1,1001))
print(min(digits))
print(max(digits))
print(sum(digits))
#7.4
for value in range(1,21):
    if value % 2 !=0:
        print(value)
#7.5
for value in range(3,31):
    if value % 3 ==0:
        print(value)
#7.6
for value in range(1,11):
    print(value**3)
#7.7
squares = [value**3 for value in range(1,11)]
print(squares)