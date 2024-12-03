# sets are used to store collections of unique items .they are unordered ,meaning elements do not follow a specific order.
my_set ={1,2,3,4,5,6}

print(my_set)
type(my_set)


#creating empty set
empty_set =set()
print(type(empty_set))

#sets eliminates duplicates 
set1 =set([1,2,3,4,5,6,6]) # converting list to set 
print(set1)


#set operations 
my_set.add(7,8,9,10)

print(my_set)

#remove 
my_set.remove(7)
print(my_set)


my_set.discard(11) # it won't gives error

# pop 

set2 =my_set.pop() # it removes first element 
print(set2)

my_set.clear() # for clearing 

#membership test 
set3 ={1,2,3,4,5,6}
print(6 in set3 ) # gives true or false 

#math operations 

set1 ={1,2,3,4,5,6,7,8,9,}
set2 ={1,2,3,4,5,6}

union =set1.union(set2) # combining elements 

#intersections 

intersection_set =set1.intersection(set2)

print(intersection_set) # only common elements 

set1.intersection_update(set2) # common elements updated into set1 


#differencr 
print(set1.difference(set2)) # removes common elements 

#symmetric diffeference 

set1.symmetric_difference(set2) # common elements removed and shows unique elements from both sets 

# set methods 

set1 ={1,2,3}
set2 ={3,4,5}

print(set1.issubset(set2)) # common values or lese gives false 
print(set1.issuperset(set2)) # checking all the elements of set2 having or not 

# eample 
# counting unique words in text 


text = "it this era of the world we need to get money to survive otherwise no one care about you "

words=text.split()


unique_words=set(words)
print(unique_words)
print(len(unique_words))