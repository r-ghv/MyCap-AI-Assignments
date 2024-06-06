#this is a program to print a sublist of positive integers from a list of integers.
list = input("Enter a list of integers seperated by a space:").split()
plist = [int(num) for num in list]
pos_list = [num for num in plist if num >= 0]
print(f"Input List: {plist}")
print(f"Output List: {pos_list}")




