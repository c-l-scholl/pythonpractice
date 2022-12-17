# number1 = 40
# number2 = 30
# product = number1 * number2

# if product <= 1000:
# 	print(product)
# else:
# 	print(number2 + number1)

# print sum of current and previous number
"""prev = 0
for i in range(0, 10):
	sum = i + prev
	prev = i
	print(sum)"""

# Print characters from a string that are present at an even index number

"""str = input("Enter a string! ")
for i in range(0, len(str)):
	if i % 2 == 0:
		print(str[i])"""

# Remove first n characters from a string

"""str = input("Enter a string! ")
n = int(input("Enter a number! "))
if n < len(str) - 1:
	print(str[n:])"""

# Check if the first and last number of a list are the same

"""numbers_x = [10, 20, 30, 40, 10]

if numbers_x[0] == numbers_x[-1]:
	print("result is True")
else: 
	print("result is False")"""

# Display numbers divisible by 5 from a list

"""num = [10, 20, 33, 46, 55]
for n in num:
	if n % 5 == 0:
		print(n)"""

# Return the count of a given substring from a string

"""str = "Emma is good developer. Emma is a writer"
sub = "Emma"

print(str.count(sub))"""

# Print the following pattern 
"""
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
"""

"""for i in range(1, 6):
	for num in range(1, i):
		print(i, end=" ")
	print("\n")"""

# Check palindrome number

"""num = 12321
temp = num
reverse = 0

while num != 0:
	digit = num % 10
	reverse = reverse * 10 + digit
	num //= 10

print(temp == reverse)"""

# Create a new list from a two list using the following condition

"""list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

list = []

for num in list1:
	if num % 2 == 1:
		list.append(num)

for i in list2:
	if i % 2 == 0:
		list.append(i)
print(list)
"""

# Extract each digit from an integer in the reverse order

"""num = 7536

while num != 0:
	print(num % 10, end=" ")
	num //= 10"""

# Calculate income tax for the given income 

"""salary = 45000
tax = 0

if salary >= 10000:
	salary -= 10000

if salary >= 10000:
	salary -= 10000
	tax = 10000 * 0.1
else:
	tax = salary * 0.1

if salary > 0:
	tax += salary * 0.2
print(tax)"""

# Print multiplication from 1 to 10

"""for i in range(1, 11):
	for j in range(1, 11):
		print(i * j, end=" ")
	print("\t\t")"""

# Print downward half-pyramid pattern with *

"""for i in range(6, 0, -1):
	for num in range(0, i - 1):
		print("*", end=" ")
	print("\n")"""

# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp

"""def exponent(base, exp):
	b = base
	e = exp
	num = b
	for i in range(e - 1):
		num *= b
	print(num)
exponent(5, 4)"""

# Create a function in python

''' def func(name, age):
    print(name, age)
    
func("Camden", 19) '''

# Create a function with a variable length of arguments

''' def func1(*args):
    for i in args:
        print(i)
        
func1(10, 20, 30, 50, 23, 61, 234, 1234) '''

# Return multiple values from a function
''' 
def calculation(a, b):
    add = a + b
    subtract = a - b
    print(add, subtract)
calculation(102, 54) '''

# 4. Create a function with a default argument

''' def show_employee(name, salary=9000):
    print(name, salary)
show_employee("Camden", 23402)
show_employee("Aaron") '''
    
# 5. Create an inner function to calculate the addition in the following way
	# Create an outer function that will accept two parameters
	# Create an inner function inside an outer function that will calculate addition
	# An outer function will add 5 to addition and return it
 
''' def func(a, b):

	def addition(a, b):
		return a + b
	num = addition(a, b) + 5
	return num
print(func(5, 3)) '''

# 6. Create a recursive function

''' def recursive(num):
	if num:
		return num + recursive(num - 1)
	else:
		return 0
print(recursive(15)) '''

# 7. Assign a new name to function and call it through the new name

''' def display_student(name, age):
    print(name, age)
    
show_student = display_student

show_student("camden", 19) '''






	
 




