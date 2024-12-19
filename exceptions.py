#Exceptions handling in python allows you to handle errors gracefully and take corrective actions without stopping the execution of the program .
#zerodivisionerror-dividing by zero
#FileNotFoundError -file not found
#ValueError-invalid value
#TypeError-invalid type 
# try ,except , block 
try:
    a=b
except:
    print("variable has not been assigned")    

try:
    a =b
except NameError as ex:
    print(ex) 

result =1/0

try:
    result =1/0
except ZeroDivisionError as ex:
    print(ex)  


try:
    result =1/0
except ZeroDivisionError as ex:
    print(ex) 
except Exception as ex1:
    print(ex1)
    print("main exception here ")  


try:
    num=int(input("enter number"))
    result =10/num
except ValueError:
    print("this is not a valid number")
except ZeroDivisionError:
    print("greater than zero")
except Exception as ex:
    print(ex)   



try:
    num=int(input("enter number"))
    result =10/num
except ValueError:
    print("this is not a valid number")
except ZeroDivisionError:
    print("greater than zero")
except Exception as ex:
    print(ex)
else:
    print(f"the result is {result}")   



try:
    num=int(input("enter number"))
    result =10/num
except ValueError:
    print("this is not a valid number")
except ZeroDivisionError:
    print("greater than zero")
except Exception as ex:
    print(ex)
else:
    print(f"the result is {result}")  
finally:
    print("complete")    

