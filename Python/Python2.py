# ## Task 2.1

#  Create a function that takes in two integers and returns
## a Boolean True if their sum is 10, False if their sum is something else.
def check_ten(n1: int,n2: int) -> bool:
    # Code Here
    return n1 + n2 == 10



# ## Task 2.2
#
# Create a function that takes in two integers and returns True if their
# sum is 10, otherwise, return the actual sum value.
def check_ten_sum(n1: int,n2: int) -> bool:
    # Code Here
    return True if n1 + n2 == 10 else n1 + n2



# ## Task 2.3
#
# Create a function that takes in a string and returns back the
# first character of that string in upper case.
def first_upper(mystring: str) -> str:
    # Code Here
    return mystring[0].upper()



# ## Task 2.4
#
# Create a function that takes in a string and returns the last two characters.
# If there are less than two chracters, return the string:  "Error".
def last_two(mystring: str) -> str:
    # Code Here
    return mystring[-2:-1] if len(mystring) > 1 else "Error"


# ## Task 2.5
#
# Given a list of integers, return True if the sequence [1,2,3] is somewhere
# in the list.
def seq_check(nums: list[int]) -> bool:
    # Code here
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return True
    return False

# ## Task 2.6
#
# Given a 2 strings, create a function that returns the difference in length
# between them. This difference in length should always be a positive number
# (or just 0).
def compare_len(s1: str, s2: str) -> int:
    # Code Here
    return abs(len(s1) - len(s1))



# ## Task 2.7
#
# Given a list of integers, if the length of the list is an even number,
# return the sum of the list. If the length of the list is odd, return the max
# value in that list.
def sum_or_max(mylist: list[int]) -> int:
    # Code Here
    if len(mylist) % 2 == 0:
        return sum(mylist)
    else:
        return max(mylist)