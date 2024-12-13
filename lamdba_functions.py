# functions without name ,used for short operation .Only one expression can have any arguments 
def addition(a,b):
    return a+b

addition(2,4)

add =lambda a,b:a+b # add is a lambda function 

print(add(2,4))

def even(num):
    if num%2==0:
        return True

even(24)

even1=lambda num:num%2==0

even1(24)

numbers=[1,2,3,4,5,6]

def square(number):
    return numbers **2
square(2)
# map() - applies a function to all items in a list 

list(map(lambda x :x**2,numbers))

