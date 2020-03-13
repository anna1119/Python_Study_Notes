# Following: Array
# ----------------------------------------------------------------------
# python is able to print out the array
names = ['Anna', 'Carina', 'Ming']
print(names)
print(names[0])

# change variable in an array
names[2] = 'Mingming'
print(names[2])

# ----------------------------------------------------------------------
# add new element at the end of an array
# use append(element)
names.append('Charmine')
print(names[3])

# insert new element at a particular index in an array
# use insert(index, element)
names.insert(1, 'Alina')
print(names)


# ----------------------------------------------------------------------
# Delete element from an array
# 1. if you know the index of the element
#    use del array[index]
#    effects: delete the element permanently, you cannot access it forever
integer_array = [1, 2, 3, 4, 5, 6]
del integer_array[5]
print(integer_array)

# 2. treat an array as a stack, use pop() to get the value of 
#    the last element and remove it from the array
#    remember that you can only access the top value
popped_num = integer_array.pop()
print(integer_array)
print(popped_num)
# if you want to delete an element at a specific index using pop
# then you only need to add the index in the bracks
first_element = integer_array.pop(0)
print(integer_array)
print(first_element)

# Conclusion: if you are not sure which method you should choose
#             1. if you only want to delete an element from an array
#                and you will not use its value, then use del
#             2. if you want to use the value of the element after
#                you delete it, then use pop


# 3. Use remove(element) when you do not know the index of the element
letters = ['a', 'b', 'c']
letters.remove('c')
print(letters)
# Warning: when the value of the element appears multiple names in the array
#          remove will only remove the first appearence of the value
#          In order to remove all, you need to use loops if you choose to use
#          remove()


# ----------------------------------------------------------------------
# Sort Array
# 1. Use array.sort() to sort an array permenantly

# This example sort an array of strings in alphabetical order
subjects = ['english', 'math', 'arts']
numbers = [3, 2, 1]
subjects.sort()
numbers.sort()
print(subjects)
print(numbers)

# This example sort the same array but in reverse order
# in order to do so, you need to use sort(reverse=True)
subjects.sort(reverse=True)
numbers.sort(reverse=True)
print(subjects)
print(numbers)

# 2. Use sorted(array) to sort an arrya temporarily
letters_array = ['b', 'a', 'c']
numbers_2 = [10, -2, 3]
print("\nThis is the original order: ")
print(letters_array)
print(numbers_2)
print("\nHere is the sorted array: ")
print(sorted(letters_array))
print(sorted(numbers_2))
print("\nHere the array is sorted in reverse order")
print(sorted(letters_array, reverse=True))
print(sorted(numbers_2, reverse=True))

# Remark: this example we used here, all the strings are in 
#         lowercase. When there are uppercase letters and 
#         lowercase letters, we need to do more complicated
#         things

# 3. Use reverse() function to reverse the order of an array
#    The last element becomes the first, the second last
#    becomes the second, so on and so forth
#    effects: change the order of the array permanently
letter_array_2 = ['t', 'o', 'p']
print(letter_array_2)
letter_array_2.reverse()
print(letter_array_2)

# 4. Use len() function to get the length of an array
# The following function should produce output 3
len(letter_array_2)

