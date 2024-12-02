# list slicing 

numbers = [1,2,3,4,5,6,7,8,9,10]

print(numbers[2:5])
print(numbers[:5])
print(numbers[5:])
print(numbers[::2])
print(numbers[::-1])

## iterating over list 

for num in numbers:
    print(num)

# iterating with index  enumerate it will gives index value 
for index ,number in enumerate(numbers):
    print(index,num)



# list comprehensions are a powerful and concise way to create lists in python 


#list comprehension
lst=[]
for x in range(10):
    lst.append(x**2)

print(lst)    


[x **2 for x in range(10)] # simplifing code 


# basic syntax [expression for item in iterable]

# with conditional logic  [expression for item in iterable if condition ]
# nested list 
# [expression for item1 in iterable for item2 in iterable]


square =[num**2 for num in range(10)]
print(square)


lst =[]
for i in range(10):
    if i%2==0:
        lst.append(i)

print(lst)

even= [num for num in range(10) if num%2==0]
print(even)


lst1=[1,2,3,4,5,6]
lst2=['a','b','c','d']

pair =[ [i,j]for i in lst1 for j in lst2]

print(pair)


words =["hello","world","python","list","compre","hension"]

lengths =[len(word) for word in words]

print(lengths)