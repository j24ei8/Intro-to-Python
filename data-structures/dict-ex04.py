# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

result = {}
n = 5

for i in range(n):
  result[i + 1] = (i + 1)**2
print(result)
