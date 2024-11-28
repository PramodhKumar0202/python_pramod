 # if condition 

num = 666666
if num>600:  # if condition is true then only it will executes 
    print("welcome")







#excutes if condition is false 

age =18

if age>=18:
    print("eligible for coming")
else:
    print("you are a minor")


#elif 
# allows to check multiple conditions 

age = 24

if age <16:
    print("child")
elif age<18:
    print("welcome to the party")
else:
    print("adult")        
# nested 
num =int(input("enter the number"))

if num>=0:
    print("number is postive")
    if num%2==0:
        print("the number is even")
    else:
        print("number is odd")
else:
    print("number is negative")

# example 
year =int(input("enter the year "))

if (year%4==0):
    if year %100==0:
        if year %400==0:
            print(year,"is a leap year")
        else:
            print(year,"not a leap year")  
    else:
        print("leap")
else:
    print("leap year") 

# example2
num1 =float(input("enter the number: "))  
num2 =float(input("enter the number: "))  
operation =input("enter operation (+,-,*,/): ") 


if operation == '+':
    result= num1 + num2
elif operation == '-':
    result =num1 -num2  
elif operation == '*':
    result =num1 *num2  
elif operation == '/':
    if num2 !=0:
       result =num1 /num2  
    else:
        result ="error ! division by zero"
else:
    result ="invalid operation"  
print("result:",result)                       