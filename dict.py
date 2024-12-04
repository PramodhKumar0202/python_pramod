# creating empty dictionary 

empty_dict={}

print(type(empty_dict))

#another way 
e_dict=dict()
print(type(e_dict))
 



student ={"name":"topg","age":24,"location":"India"}
print(student)

#single key is always used  key is always unique 

student ={"name":"topg","age":24,"name":"India"}


#accessing elements
student ={"name":"topg","age":24,"location":"India"} 
print(student["age"])
print(student("location"))


#updating 
student["age"]=30
student["name"] ="pramod"

#deleting 

del student['name']
# dict methods 

keys =student.keys()
print(keys)

values = student.values()
print(values)

items =student.items()
print(items)


#shallow copy method
student_copy=student
print(student)
print(student_copy)

student["name"]="topg"
print(student)
print(student_copy)



student1=student.copy()
student=["name"]="pramod"
print(student)
print(student1)


#iterating dictionaries 

for keys in student.keyes():
    print(keys)


for values in student.values():
    print(values)



for key, value in student.items():
    print(f"{key},{value}")





