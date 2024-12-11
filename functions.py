# function is a block of code ,perform specific task and reusing code 
#syntax
def function_name (parameters):
    """ function details"""
    #function body
    return expression 

## why function 

num =24
if num%2==0:
    print("even number")
else:
    print("odd number ")


#function 


def eve_or_odd(num):
    if num%2==0:
        print("number is even")
    else:
        print("number is odd")

#calling functions 

eve_or_odd(20)

# function with multiple parameter

def add(a,b):
    return a+b
result =add(2,4)

print(result)


#default parameter

def greet(name):
    print(f"hello{name}")

greet("pramod")






def greet(name="topg"):
    print(f"hello{name}")

greet("pramod")


# variable length arguments 
#positional and keywords arguments 

def print_number(*args):
    for num in args:
        print(num)

print_number(1,2,3,4,5,6)


# keywords arguments 
def details(**kwargs):
    for key , value in kwargs.items():
        print(f"{key}:{value}")

details(name="topg",age="24",country="usa")     







def details(*args,**kwargs):
    for val in args:
        print(f" positional arguments :{val}")

    for key , value in kwargs.items():
        print(f"{key}:{value}")




details(1,2,3,4,5,6,name="topg",age="24",country="usa")  






#return statement 
def multi(a,b):
    return a*b

multi(2,4)




# return multiple parameters 
def multi(a,b):
    return a*b,a

multi(2,4)
