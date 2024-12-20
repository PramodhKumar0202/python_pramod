#read a whole file 
with open('text.txt','r') as file:
    content =file.read()
    print(content)

# reading file line by line 
with open('text.txt','r') as file :
    for line in file:
        print(line.strip())

#writing a file 
with open('example.txt','w') as file :
    file.write('hello world')
    file.write('topg') 

#without overwriting 
with open('example.txt','a') as file:
    file.write("append operation")

# writing list of lines 
lines =['first line\n','second line\n','third line\n']
with open('example.txt','a') as file:
  file.writelines(lines)

#binary files 

