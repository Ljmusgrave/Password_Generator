"""Write a password generator in Python. Be creative with how you generate passwords
 - strong passwords have a mix of lowercase letters, uppercase letters, numbers,
 and symbols. The passwords should be random, generating a new password every
 time the user asks for a new password."""

import random
import string

# These allow me to change the length of the password, the amount of type of characters used, and the
# minimum amount needed of each given character (will CRASH if total amount of needed given
# characters exceeds password_len)
password_len = random.randint(16, 20)
num_of_type = len(["lowercase letters", "uppercase letters", "numbers", "punctuation"])
min_needed_char = 2
final_password = ""


# Chooses a random amount of characters for each type called
def amount_of_character():
    global password_len
    global num_of_type
    total_amount = random.randint(min_needed_char, (password_len - (num_of_type * min_needed_char)))
    # Tells the function that 1 type is assigned/"done" for each time the function is called
    num_of_type -= 1
    # Subtract from password_len to keep track of characters chosen
    password_len -= total_amount
    return total_amount


# var1, var2, etc. quickhand way of assigning a name to each type of character
# Uses above function for each type of character
var1_count = amount_of_character()
var2_count = amount_of_character()
var3_count = amount_of_character()
# var4 needs to use all remaining spaces of password_len
var4_count = password_len


# Adds random character to password
def generate_password(type_char):
    global final_password
    final_password += type_char


# Maybe I could shorten this section by using another function and a dictionary that ties var# to its given
# random selection? I don't know how to keep the random selection random if I assign it to anything like a
# variable or dictionary though...
while var1_count > 0:
    # I use strings.digits instead of random.randint() so it is treated as a string and not an int
    generate_password(random.choice(string.digits))
    var1_count -= 1

while var2_count > 0:
    generate_password(random.choice(string.ascii_lowercase))
    var2_count -= 1

while var3_count > 0:
    generate_password(random.choice(string.ascii_uppercase))
    var3_count -= 1

while var4_count > 0:
    generate_password(random.choice(string.punctuation))
    var4_count -= 1

# Shuffles characters of password so not in order of digits -> lowercase -> uppercase -> punctuation
list1 = list(final_password)
random.shuffle(list1)
final_password = "".join(list1)

# This is your final product: a generated password
print(final_password)
