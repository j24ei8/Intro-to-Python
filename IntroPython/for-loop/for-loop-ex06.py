# Exercise 6: Print the following pattern
# Write a program to print the following start pattern using the for loop

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(1, 6):
  for j in range(1, i + 1):
    print("*", end=" ")
  print()

for i in range(4, 0, -1):
  for j in range(1, i + 1):
    print("*", end=" ")
  print()

  # for j in range(1, i - 1):
  #   print(j, end=" ")

