# Implement an algorithm to determine if a string has all unique characters.
any_String = input("Enter any string: ")
distinct_chars = any_String.upper()
distinct = set(distinct_chars)
if(len(distinct) == len(any_String)):
    print(True)
else:
    print(False)
