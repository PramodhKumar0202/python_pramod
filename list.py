# lists 

lst =[]
print(type(lst)) # for creating empty list 


names =["topg ","pramod",1,2,3,4,5,6] # we can store all types of values
print(names)


mixed_names =["topg","pramod",5.16,True] #all types of data types 

print(mixed_names)


#accessing list 

fruits =["apple","banana","pineapple","kiwi"]
print(fruits[0]) # accessing using index values 
print(fruits[2])
print(fruits[-1]) # prints kiwi


print(fruits[1:])
print(fruits[1:4])


#modifying list 
fruits [1] = "avacado"

fruits[1:]="avacado"


fruits.append ("orange") # add amn item to the end
print(fruits)


fruits.insert(1,"watermelon")
print(fruits)


fruits.remove("avacado")


pop_fruit =fruits.pop() #removes the last element
print(pop_fruit)
print(fruits)


index=fruits.index("kiwi") #getting index

fruits.insert(2,"avacado")
print(fruits.count("avacado"))

fruits.sort()

fruits.reverse() # reverse the list


 
fruits.clear()

