# class is ablue print for creating objects , atributes,methods
class Car:
    pass

audi=Car()
bmw =Car()




audi.windows=4
print(audi.windows)

tata =Car()
tata.doors=4
print(tata.windows)

# instance variables and methods
class Dog:
    # constructor 
    def __init__(self,name,age):
        self.name=name
        self.age=age
        pass
#create objects   
dog1=Dog("loki",2) 
print(dog1)
print(dog1.name)
dog2=Dog("lucy",6)

#instance methods 
class Dog:
   def __init__(self,name,age):
       self.name=name
       self.age=age
   def bark(self):
       print(f"{self.name} says woof")  

dog3=Dog("buddy",6)
dog3.bark()
dog4=Dog("loki",6) 
dog4.bark()

#modeling  a bank
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
        pass
    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} is deposited")

    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient funds!") 
        else:
            self.balance-=amount
            print(f"{amount} is withdrawn. new balance is {self.balance}")       
    def get_balance(self):
        return self.balance
    
account=BankAccount("topg",660)
print(account.balance)
#account.deposit(60000)
#account.balance
#account.deposit(6)
#account.withdraw(2)