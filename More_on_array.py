# Array

#---------------------------------------------------------------------------
# Use for loop to go through an array
# do not forget the colon 
# The following example prints every name in the names array
# For code in the for loop, it will be execute (lengh) times
# For code outside the for loop, it will only be execute one time
names = ['Anna', 'Bob', 'Alex', 'Allen']
for name in names:
    print(name)
print("Welcom, everyone!")

#---------------------------------------------------------------------------
# Use range() to create an array
# You can use for loop and range() function to generate an array of numbers
# The following code will print integers 1, 2, 3, 4 using range()
# Warning: for range(a, b), it will start from a and end before b
#          it will never reach b!
for value in range(1, 5):
    print(value)

# You can use list() and range() to create an array of integers
numbers = list(range(1, 5))
print(numbers)

# You can set how much to increase each time
# range(a, b, c): a is the start point
#                 b is the end point (will end before b)
#                 c is how much to increase
# This example create an array that includes even numbers between 
# 2 and 11 (not include)
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# This example creates an array of the squares
squares_array = []
for num in range(1, 11):
    squares_array.append(num**2)
print(squares_array)

# Alternative method to create such an array
squares_array_2 = [value**2 for value in range(1, 11)]
print(squares_array_2)

# You can apply min, max and sum functions on an array of numbers
num_arr = [3, 2, 1, 0, -1]
print(min(num_arr))
print(max(num_arr))
print(sum(num_arr))

#---------------------------------------------------------------------------
# This part introduces how to do array slicing
# In order to get part of the array, we need to know the stard point and end
# point. Here, for the end point, it works the same way as range(), the function
# stops right before the end point
# The format is [startIndex:endIndex]
# If you do[:endIndex], then python will automatically starts from index 0
# If you do[startIndex:], then python will authomatically ends at the end
letter = ['a', 'b', 'c', 'd', 'e']
print(letter[0:3]) # ['a', 'b', 'c']
print(letter[2:4]) # ['c', 'd']
print(letter[:4])  # ['a', 'b', 'c', 'd']
print(letter[2:])  # ['c', 'd', 'e']

# For negative index, it means that start from the end of the array and move
# backward
# If you want the get the last three letters, you can 
print(letter[-3:]) # ['c', 'd', 'e']

# You can apply for loop on the slicing of an array
for lett in letter[0:3]:
    print(lett)

# Make a copy of an array using [:]
# If you simply assign the value of my_num to friend_num, they will mean the same array
# when you change my_num or friend_num, the array will always be changed
my_num = [1, 2, 3]
friend_num = my_num[:]
print(my_num)
print(friend_num)


#---------------------------------------------------------------------------
# This part introduces tuples
# In order to define a tuple, we use parentheses
# In order to get a single value, it works the same way as array does
# One property that differs tuples from array is that the value in 
# tuples cannot be changed
dimension = (10, 20)
print(dimension[0]) # 10
print(dimension[1]) # 20

# If you try dimension[0] = 30, python will give you an error message since
# tuple object does not support item assignment. However, you can change
# tuple as a whole
dimension = (30, 30) 
# this is valid in python since you change dimension as 
# a whole instead of changing one specific item in it

# You can apply for loop on tuples, same as array
for num in dimension:
    print(num)
