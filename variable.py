#Variable definition
#Variables are fundamental elements in programming used to store data that can be referenced and manipulated in a program.
#In Python, variables are created when you assign a value to them, and they do not need explicit declaration to reserve memory space. 

# declaring and assigning variables
name ="python"
age =24
location ="India"
is_student =True

# printing variables 
print("name :", name)
print("age :", age)
print("location:", location)
# Important points to remember while creating variables 

## Variable names should be descriptive
## They must start with a letter or an '_' and contains letter,numbers and underscores
## variables names case sensitive

# example
first_name =" pramodh"

# invalid variables
#6age =24
#first-name ="python"
# $location = "India"

# case sensitivity 
name ="pramod"
Name ="kumar"

# varibles types 
# python is dynamically typed ,type of variable is determined at run time 
age =24 # int 
name ="pramod" # string 
height =5.10 # float
is_student =True # boolean

# checking varible type
print(type(age))

# type converion 
age =24

age_str =str(age) # converts into string

num ='24'

num1 =int(num) # converting into int

num2 =float(age) # converting into float 
 # we can convert int to float and vice versa 

name ="python"

name1 =int(name) # we can't convert 


# Dynamic Typing
# Python allows the type of a vraible to change as the program executes

val=10 #int
print(val,type(val))

val="Hello"
print(var,type(val))

val=3.14
print(val,type(val))
