#20.6
#1
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n - 1)
print(factorial(n=10))
#2
def fibonacchi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacchi(n-1)+fibonacchi(n-2))
print(fibonacchi(7))
#3
pr=lambda x, y: x*y
result = pr(int(input('Введите первое число: ')), int(input('Введите второе число: ')))
print('Произведение этих чисел равно: ',result)
#4
a = 'Первая строка'
b = 'вторая строка'
с = 'трЕтья стРока'
strs = [a,b,с]
STRS = map(lambda x: x.upper(), strs)
print(list(STRS))
#5
a = '123'
b = 'вторая'
c = 'трЕтья стРока'
d = 'Четвёртая строка'
strs = [a,b,c,d]
for x in strs:
    if len(x) >  3:
       print(x.upper())
#6
num1 = [1,2,3,4,5,6,7,8,9]
num2 = [9,8,7,6,5,4,3,2,1]
num = zip(num1,num2)
nums = list(num)
print(nums)
#7
names = [1,2,3,4]
ages = [4,5,12,45]
for name in zip(names, ages):
    numes = list(name)
    print(sum(numes))
#8
sds = [1,2,3,4,5,6,7]
sms = ['Маша','Петя','Вася','Коля','Даша','Максим','Эдик']
sss = list(zip(sms,sds))
print(sss)
sks,sfs = zip(*sss)
print(sks)
print(sfs)

