# converting temparature 
def convert_temp(temp,unit):
    if unit == 'C':
        return temp *9/5 +32 # celsius to fahrenheit
    elif unit == 'F':
        return (temp -32) *5/9 # Fahrenheit to celsius
    else:
        return None

convert_temp(25,'C')

# example 2 password checker 
def is_strong(password):
    if len(password) <8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$%^&*()_+' for char in password):
        return False
    return True

print(is_strong("pramodh$6"))

#example3 total items 
def total_cost(cart):
    cost=0
    for item in cart:
        cost+=item['price'] * item['quantity']
    pass

cart =[
    {'name':'apple','price':0.6,'quantity':6},
    {'name':'banana','price':0.4,'quantity':12}
]

print(total_cost(cart))

#example 4 palindrome =aba=aba
def is_palidrome(s):
    s =s.lower().replace(" ","")
    return s==s[::-1]
print(is_palidrome("A man a plan a canal panama"))

#example 5 factorials of a number using recursion
def factorial(n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)

print(factorial(6))    

#example 6 read file and count the frequency of each word
def count_word(file_path):
    word_count={}
    with open(file_path,'r') as file:
        for line in file:
            words =line.split()
            for word in words:
                word=word.lower().strip('.,!;:"\'')
                word_count[word] =word_count.get(word,0)+1
    return word_count

filepath ='sample.txt'
word_frequency =count_word(filepath)
print(word_frequency)            

# email checking 
import re 

def valid_email(email):
    pattern =r'^[a-zA-Z0-9_.+=]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern,email) is not None

print(valid_email("topg@gmail.com"))