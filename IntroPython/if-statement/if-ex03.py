# Write a Python program to find the median of three values.
# Expected Output:

# Input first number: 15                                                  
# Input second number: 26                                                 
# Input third number: 29                                                  
# The median is 26.0 

# val = input("Please type anything")
# print("this is your input:", val)

val1 = input("Please type a number")
val2 = input("Please type your second number")
val3 = input("Please type your third number")

if val2>val1 and val2<val3:
  print("val2 is the median")
elif val1>val2 and val1<val3:
  print("val1 is the median")
else:
  print("val3 is the median")