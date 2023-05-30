'''

Criteria to generate password-
* Atleast 14 characters
* Atleast 1 Uppercase
* Atlease 1 Lowercase
* Atleast 1 symbol
* Atleast 1 number

'''

import string
import random

l_alphabets = string.ascii_lowercase
print(l_alphabets)
u_alphabets = string.ascii_uppercase
symbols = string.punctuation
print(symbols)
number = "".join([str(num) for num in range(10)])
print(number)

#Atleast 1 of each variable in a list

randome_atleast = [random.choice(u_alphabets),
                   random.choice(l_alphabets),
                   random.choice(symbols),
                   random.choice(number)]

# print(randome_atleast)

#remainig

listed = f"{l_alphabets}{u_alphabets}{symbols}{number}"


remaining= random.sample(listed,10)
# print(remaining)

combine = randome_atleast+remaining
random.shuffle(combine)

result  = ''.join(combine)
print(result)


