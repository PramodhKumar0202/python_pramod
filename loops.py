# loops 
#for i in range(0,10):
 #   print(i)


# in range last number is not printed 

for i in range(0,10,1): # step size 1 means increments 1 value 
    print(i)

for i in range(0,10,2): # step size 2 means increments 2 value 
    print(i)


for i in range(10,0,-1): # prints reverse 
    print(i)

str ="pramod"

for i in str: # prints each charachter 
    print(i)


# while loop 
# continues to executes as long as consition is true 
count=0

while count<5:
    print(count)
    count=count+1

count =0

while count%2==0:
    print(count)
    count=count+1





#loop control stmnts 
# break ,exits the loop 


for i in range(10): # it will prints 6 , once 7 comes it will exist the loop
    if i ==7:
        break
    else:
        print(i)



# continue ,skips current iteration and continues with the next

for i in range(10): # it will prints only odd numbers 
    if i%2==0:
        continue
    print(i)


#pass ,null operation ,it does nothing 
for i in range(7):
    if i==7:
        print("the number is",i)
        pass
    print(i)

# nested loops
# loop inside a loop
for i in range(7): # each element in i will be printed two times 
    for j in range(2):
        print(f"i:{i} and j:{j}")  


#example 

n=10
sum=0
count=1

while count<=n:
    sum=sum+count
    count=count+1
print("sum of number:", sum)    


n=10
sum=0

for i in range(11):
    sum=sum+i
print(sum)    

# prime numbers 
for num in range(1,100):
    if num>1:
        for i in range(2,num):
            if num%i==0: # this condition is true is not a prime number 
                break
        else:
            print(num)    