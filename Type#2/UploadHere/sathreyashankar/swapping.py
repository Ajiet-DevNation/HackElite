# Given two values of the same type, swap both the values

first = input("Enter first value: ")
second = input("Enter second value of the same type of first: ")
print("Before Swapping\na = ", first, "b = ", second)
first, second = second, first
print("After Swapping\na = ", first, "b = ", second)