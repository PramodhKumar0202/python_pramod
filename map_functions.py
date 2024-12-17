# map() function applies a given function to all items in an input list  and retunrs a map object .this is useful for transforming data in alist comprehensively
def square(x):
    return x*x

square(6)
# using map
numbers =[1,2,3,4,5,6]
list[map(square,numbers)]

#lambda function with map
numbers =[1,2,3,4,5,6]
list(map(lambda x:x*x,numbers))


#map multiple iterables 
numbers1 =[1,2,3,4,5,6]
numbers2 =[7,8,9,10,11,12]

added_num =list(map(lambda x,y:x+y,numbers1,numbers2))
print(added_num)

# converting numbers 
str_num =['1','2','3','4','5','6']
int_num =list(map(int,str_num))

print(int_num)

words =['apple','kiwi','banana','avacado']
upper_word =list(map(str.upper,words))
print(upper_word)

def get_name(person):
    return person['name']

people =[
    {'name':'top g','age':24},
    {'name':'pramod','age':30}
]    

list(map(get_name,people))