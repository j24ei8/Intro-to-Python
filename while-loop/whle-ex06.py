# Write a Python program to get the Fibonacci series between 0 and 50.
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34


n_prev_prev = 0
n_prev = 1
print(n_prev_prev, n_prev, end=" ")
num = 0
while n_prev_prev + n_prev >= 0 and n_prev_prev + n_prev <= 50:
  num = n_prev + n_prev_prev
  print(num, end=" ")
  n_prev_prev = n_prev
  n_prev = num
  