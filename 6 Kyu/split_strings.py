# Complete the solution so that it splits the string into pairs of two characters. 
# If the string contains an odd number of characters then it should replace the missing 
# second character of the final pair with an underscore ('_').

def solution(s):
    result = []
    
    for i in range(0, len(s), 2):  # It starts at index 0 and advances by 2.
        pair = s[i:i+2]

        if len(pair) < 2:   # If the pair has fewer than 2 characters (last iteration)
            pair += "_"
        
        result.append(pair)
    
    return result

# Tests
print(solution("asdfadsf")) # ['as', 'df', 'ad', 'sf']
print(solution("asdfads"))  # ['as', 'df', 'ad', 's_']
print(solution(""))         # []
print(solution("x")) # ['x_']
