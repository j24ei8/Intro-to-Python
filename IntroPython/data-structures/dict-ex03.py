# Write a Python script to check whether a given key already exists in a dictionary.

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

given = 4

# print(d.items())
# print(d.keys())
# print(d.values())

print("list(d):", list(d))

if given in list(d):
  print("value exsits")
else:
  print("value does not exsits")
