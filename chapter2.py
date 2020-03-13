
# Following: Knowledge about string
# -------------------------------------------------------------------------
# uppercase and lowercase practice

# title() function changes the first letter of each word to uppercase
# upper() function changes all letters to uppercase
# lower() function changes all letters to lowercase
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())


# combine strings
# python uses + to combine strings
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")


# use \t to indent 
# use \n to change to a newline
print("python")
print("\tpython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")


# to delete whitespace at the end of a string, use rstrip()
favourite_language = 'python  '
favourite_language.rstrip()
# if you only do things until this point, when you check
#  favourite_language again, it still has whitespace at the end
#  in order to make permanent change, you need to change the variable
favourite_language = favourite_language.rstrip()

# if you want to delete whitespace at the beginning of the string
# use lstrip()
# if you want to delete whitespace at both sides, use strip()
favourite_language = ' python '
favourite_language = favourite_language.strip()
print(favourite_language)

# in order to use quotation mark in a string, you need to use " "
message = "Bob's name" # valid
# message = 'Bob's name' invalid since python cannot determine
# where is the end of the string
# -------------------------------------------------------------------------


# Following: Numbers
# -------------------------------------------------------------------------

# python uses ** to calculate powers of a number
# you can use parenthesis to specify the order of operations
3 ** 2 #9

# python has floating point, but it sometimes can be inexact
# avoid using floating point
float_example = 2.1

# change numbers to strings use function str(number)
age = 18
change_number_to_string = "Happy " + str(age) + "rd birthday!"

# when you use division, python2 rounds towards 0
division_example = 3 / 2 # 1
print(division_example)
