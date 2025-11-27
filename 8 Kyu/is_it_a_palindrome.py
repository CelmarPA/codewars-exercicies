# Write a function that checks if a given string (case insensitive) is a palindrome.

# A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards, such as madam or racecar.

def is_palindrome(s):
    return True if s.lower() == s[::-1].lower() else False


# Tests
print(is_palindrome('a'))      # True
print(is_palindrome('aba'))    # True
print(is_palindrome('Abba'))   # True
print(is_palindrome('malam'))  # True
print(is_palindrome('walter')) # False
print(is_palindrome('kodok'))  # True
print(is_palindrome('Kasue'))  # False
