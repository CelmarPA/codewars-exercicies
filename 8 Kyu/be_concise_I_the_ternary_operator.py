# Be Concise I - The Ternary Operator
# You are given a function that takes a parameter age (which will always be a positive integer) and does the following:

# If the age is 12 or lower, it return "You're a(n) kid"
# If the age is anything between 13 and 17 (inclusive), it return "You're a(n) teenager"
# If the age is anything between 18 and 64 (inclusive), it return "You're a(n) adult"
# If the age is 65 or above, it return "You're a(n) elderly"
# Your task is to shorten the code as much as possible. Note that submitting the given code will not work because there is a character limit of 145.

# I'll give you a few hints:

# The title itself is a hint - if you're not sure what to do, always research any terminology in this description that you have not heard of!
# Don't you think the whole "You're a(n) <insert_something_here>" is very repetitive? ;) Perhaps we can shorten it?
# Write everything in one line, \n and other whitespaces counts.
# Whatever you do, do not change what the function does. Good luck :)

def describe_age(a):return"You're a(n) "+("kid"if a<13 else"teenager"if a<18 else"adult"if a<65 else"elderly")

# describe_age = lambda n: "You're a(n) " + "kid teenager adult elderly".split()[(n>12) + (n>17) + (n>64)]

# Tests
print(describe_age(9))     #"You're a(n) kid"
print(describe_age(10))    #"You're a(n) kid"
print(describe_age(11))    #"You're a(n) kid"
print(describe_age(12))    #"You're a(n) kid"
print(describe_age(13))    #"You're a(n) teenager"
print(describe_age(14))    #"You're a(n) teenager"
print(describe_age(15))    #"You're a(n) teenager"
print(describe_age(16))    #"You're a(n) teenager"
print(describe_age(17))    #"You're a(n) teenager"
print(describe_age(18))    #"You're a(n) adult"
print(describe_age(19))    #"You're a(n) adult"
print(describe_age(63))    #"You're a(n) adult"
print(describe_age(64))    #"You're a(n) adult"
print(describe_age(65))    #"You're a(n) elderly"
print(describe_age(66))    #"You're a(n) elderly"
print(describe_age(100))   #"You're a(n) elderly"
