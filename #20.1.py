#20.1.1
x=10
def local_scope():
    x=5
    print(x)
local_scope()
print(x)
#20.1.2
def outer():
    y=20
    def inner():
        nonlocal y
        y=52
    inner()
    print(y)
outer()
#20.1.3
z=1
def modify():
    global z  
    z = 30
    z_local=7
    print(z)
    print(z_local) 
modify()    
#20.1.4
list = [1,2,3,4,5,6,7,8,9,0,12,14,46,457,75869,6796,785,654,6,46,3446,45,4,7]
def check_built_in(my_list):
    return len(my_list)
my_list = list
print(check_built_in(my_list))
#20.1.5
list = [1,2,3,4,5,6,7,8,9,0]
total = 0
def calculate_sum(numbers):
    global total 
    sum_of_numbers = sum(numbers)
    total = 100 - sum_of_numbers 
    return sum_of_numbers
numbers = list
print(calculate_sum(numbers))
