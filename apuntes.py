#Logical Operators

#n%2 == 0 or n%3 == 0 
    # is true if either or both of the condition is true, if the number is divisible by 2 or 3

#Conditional Excecution

x=1
if x > 0:
    print('x is positive')
x = -1
if x < 0:
    pass #Need to handle negative values!
    print ("Im handling negative values")

#Alternative Execution if else
x = 5
if x % 2 == 0:
    print('x is even')
else:
    print('x is odd')

#Chained Conditionals if elif else
 
x=3 
y=3

if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are iqual')

#Nested Conditionals 
if x == y:
    print('x and y are iqual')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

#EXAMPLES

if 0 < x:
    if x < 10:
        print('positive number')

if 0 < x and x < 10:
    print('same result as above')

if 0 < x < 10:
    print('same result as abobe, python option')

# Recursion
# If n is negative, it outputs the word, "END!" Otherwise, it soutputs n and then calls a function
# named countdown --itself-- passins n-1 as an argument 
def countdown(n):
    if n <= 0:
        print('END!')
    else:
        print(n)
        countdown(n-1)
countdown(10)        

# Another example
#
# If n <= 0 the return statement exits the function. The rest of the function, displays the string and
#  then call itself to dysplay n-1
#
def print_n(string, n):
    if n <= 0:
        return
    print(string +" " + str(n))
    print_n(string, n-1)

print_n("Hello from recursion", 1)

# Infinite Recursion
# In most programing environment, infinite recursion does not realy run forever. 
# Python reports an error messase when the limit is reached. 

#KEYBOARD INPUT
# In Python 2, the same function is called raw_input

print("Type some text")
#text = input()
#print('you typed '+ text)

# BOOLEAN FUNCTIONS

def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False
#
# CHECKING TYPES 
#      
def factorial(n):
    space = ' ' * (4 * n)
    if not isinstance(n, int):
        print('Factorial is only defined for integers')
        return None
    elif n < 0 :
        print('Factorial is not defined for negaive integers')
    elif n == 0:
        print(space, 'returning 1')
    else:
        print(space + n * factorial( n -1 ))

      
# THE WILE STATEMENT

def countdown_while(n):
    while n > 0:
        print(n)
        n = n -1
    print("END! while countdown")

countdown_while(10)

#break
def while_break():
    while True:
        print("Type some text. Type 'done' to end.")
        line = input()
        if line =='done':
            break
    print(line)
    print("Done")

#while_break()

# STRING

fruit = 'raspberry'
print (fruit[1])
#length
print (len(fruit))
#loop 
index = 0
while index < len(fruit):
    letter=fruit[index]
    print(letter)
    index +=1 # or index = index + 1
#other way to do same as above
for letter in fruit:
    print(letter)

# String slice
string = "Learning python"
print(string[:8])
print(string[9:])
# String are immutable, can`t do string[1]='a'

#searching string
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1

find("Hola from Python", 'H')

#String methods
word = "python"
print(word.upper())

# In operator

def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)

in_both("Hdola", "H1la")

#String comparison
word1="hola"
word2 ="hola"
if word1 == word2:
    print("Are iqual")