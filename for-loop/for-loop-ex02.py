# Exercise 2: Print the following pattern
# Write a program to use for loop to print the following reverse number pattern

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1, 6):
  print("i is ", i)
  for j in range(1, i + 1):
    print(j, end=" ")
  print()
