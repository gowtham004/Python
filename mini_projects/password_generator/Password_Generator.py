# alphabets = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
import random

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
random.shuffle(alphabets)
# numbers = [str(i) for i in range(10)]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

num_of_alphabets = int(input("Enter the num of Char you need in your Password : "))
num_of_numbers = int(input("Enter the count of numbers you need in your Password : "))
num_of_specialChar = int(input("Enter the num of Special Char you need in your Password : "))

password_list = []
for char in range(0, num_of_alphabets):
    password_list.append(random.choice(alphabets))

for char in range(0, num_of_numbers):
    password_list.append(random.choice(numbers))

for char in range(0, num_of_specialChar):
    password_list.append(random.choice(special_characters))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
print(password)
