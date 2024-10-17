#8.5.1
def summ():
    a=int(input('Введите первое число: '))
    b=int(input('Введите второе число: '))
    return a+b
print(summ())
#8.5.2
def evens(nums):
    return[num for num in nums if num %2 == 0]
nums = [1,2,3,4,5,6,7,8,89,0,]
even=evens(nums)
print(even)
#8.5.3
def srs(sr):
    summa=sum(sr)
    srednee=len(sr)
    return summa/srednee
sr=[1,2,3,4,5,6,7,8,9,15]
sredne=srs(sr)
print(sredne)
#8.5.4
string="КанагатТандырылМагандыкТарыныздан"
skip='а'
resultat=""
for bukva in string:
    if bukva == skip:
        pass
    else:
        resultat += bukva
print(resultat)        