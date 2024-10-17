#17.5.1
chet = {2,4,6,8,10,12,14,16,18,20}
nechet = {1,3,5,7,9,11,13,15,17,19}
print(chet)
print(nechet)
#17.5.2
dv = chet|nechet
print(dv)
#17.5.3
num = {1,2,3,4,5,6,7,8,9,10}
nom = {5,6,7,8,9,10,11,12,13,14,15}
num &= nom
print(num)
#17.5.4
num = {1,2,3,4,5,6,7,8,9,10}
nom = {5,6,7,8,9,10,11,12,13,14,15}
num-=nom
print(num)
#17.5.5
num = {1,2,3,4,5,6,7,8,9,10}
nom = {5,6,7,8,9,10,11,12,13,14,15}
nim=num^nom
print(nim)
#17.5.6
def proverka(chs,ch):
    if ch in chs:
        print('Число в спискке.')
    else:
        print('Число не в списке.')
chs = {1,2,3,4,5,6,7,8,9,0}
ch = int(input('Введите число: '))   
proverka(chs,ch)    
#17.5.7
chisla = {1,2,3,4,5,6,7,8,9,10}
chisla.discard(5)
print(chisla)
#17.5.8
def zipka(sps , psp):
    scs = list(zip(sps, psp))
    print(scs)
sds = {1,2,3,4,5}
sfs = {6,7,8,9,0}
zipka(sds,sfs)
#17.5.9
sps = [1,2,3,4,5,6,7,8,9,9,8,7,5,3,2]
sds = set(sps)
print(sorted(sds))
#17.5.10
def proverka(set1,set2):
    print("'True' = первое множество является подмножеством второго." )
    print("'False' = первое множество не является подмножеством второго")
    print(set1.issubset(set2))  
set1 = {4,6}
set2 = {2,4,6,7}
proverka(set1,set2)