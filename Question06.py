import sys
value =input("Enter Value:")

print("Value is :",value)
print("Value is:",type(value))
print("memory Address:",id(value))
print("size in byte:",sys.getsizeof(value))
