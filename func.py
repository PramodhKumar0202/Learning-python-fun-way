def name(num1,num2):
    print(num1+num2)
name(66,66)    



def sum(n1,n2):
    return n1+n2
total = sum()
print(sum(66,66))

def hello():
    print("hello world")
hello()   
def sum(n1,n2):
    print(n1+n2) 
sum(66666,6666)    
def sum(n1,n2):
    if (type(n1) is not int or type(n2) is not int):
        return
    return n1+n2
total =sum(6666666,66666)
print(total)
def multiple_items(*args):
    print(args)
    print(type(args))
multiple_items("pra","mod")    
def multilines(**kwargs):
    print(kwargs)
    print(type(kwargs))
multilines(name="pra",name1="mod")
#recursion 
def add_one(num):

    if (num>= 9):
        return num + 1
    total =num + 1
    print(total)

    return add_one(total)

my_total =add_one(0)
print(my_total)
value = "y"
count = 0

while value:
    count +=1
    print(count)
    if(count ==6):
        break
    else:
        value = 0
        continue
#lambda
def square(num): return num * num
#lambda num : num *num 
print(square(10000))
def addtwo(num):return num +2
#lambda num + num +2
print(addtwo(6))
#lambda a,b : a+b 
def func(x):
    return lambda num:num + x

addten= func(10)
addtwenty= func(20)

print(addten(6))
print(addtwenty(6))

numbers =[1,2,3,4,5,6]
square_num =map(lambda num: num *num ,numbers)
print(list(square_num))
lambda num : num % 2 !=0
odd_nums =filter(lambda num: num %2 !=0,numbers)
print(list(odd_nums))



