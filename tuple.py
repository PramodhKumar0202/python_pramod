# immutable and ordered collections of items 

empty_tuple =()
print(type(empty_tuple)) # creating empty tuple 


lst =list() # empty list 
tpl =tuple() # another way of creating 

numbers = tuple([1,2,3,4,5,6])


list((1,2,3,4,5,6))

mixed_tuple =(1,"hello",3.14,True)


# accessing elements 

# indexing similar like list 

# tuple operations 
concatenation =numbers + mixed_tuple
print(concatenation)

numbers *3

#immutable nature of tuple 

lst =[1,2,3,4,5,6]
lst[1]="pramod" # we can change in list 

numbers[1]= "pramod" # error tuple we can't change element 

numbers.count(1) 
numbers.index(2)

#packing and unpacking tuple 

pack_tuple =1,"hello",3.14 # whenever you create like this it will tuple 

#unpacking tuple 
a,b,c =pack_tuple
print(a)
print(b)
print(c)



