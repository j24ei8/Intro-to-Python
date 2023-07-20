# Create a list by picking an odd-index items from the first list and even index items from the second
# Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.

# Given:
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

# Expected Output:
# Element at odd-index positions from list one
# [6, 12, 18]
# Element at even-index positions from list two
# [4, 12, 20, 28]
# Printing Final third list
# [6, 12, 18, 4, 12, 20, 28]

l3 = []

for i in range(0, len(l1)):
  if i % 2 == 1:
    l3.append(l1[i])

for i in range(0, len(l2)):
  if i % 2 == 0:
    l3.append(l2[i])

print(l3)