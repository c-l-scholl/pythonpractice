import random

#A function do shuffle all the characters of a string

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here

#Generate uppercase letters

uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)

#Generate lower case letters

lowercaseletter1 = chr(random.randint(97, 122))
lowercaseletter2 = chr(random.randint(97, 122))

#Generate numbers

number1 = chr(random.randint(48,57))
number2 = chr(random.randint(48,57))

#Generate special characters

specialchar1 = chr(random.randint(33, 148))
specialchar2 = chr(random.randint(33, 148))


#Generate password using all the characters, in random order

password = uppercaseLetter1 + uppercaseLetter2 + lowercaseletter1 + lowercaseletter2 + number1 + number2 + specialchar1 + specialchar2
password = shuffle(password)

#Ouput

print(password)