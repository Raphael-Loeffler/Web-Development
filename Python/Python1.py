## Task 1.1

# Given the string:
s = 'flask'

# Use indexing to print out the following:
# 'f'
print(s[0])
# 's'
print(s[1])
# 'ask'
print(s[2:5])
# 'las'
print(s[1:4])
# 'k'
print(s[-1])
# Bonus: Use indexing to reverse the string
print(s[::-1])
## Task 1.2

# Given this nested list:
mylist = [3,7,[1,4,'hello']]

# Reassign "hello" to be "goodbye"
mylist[-1][-1] = 'goodbye'
print(mylist)
## Task 1.3

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}
print(d1.get('simple_key'))

d2 = {'k1':{'k2':'hello'}}
print(d2.get('k1').get('k2'))
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3.get('k1')[0].get('nest_key')[-1][0])

## Task 1.4

# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
print(set(mylist))

## Task 1.5

# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"
print(f"Hello my dog's name is {name} and he is {age} years old")