# separate positive and negative number from a list.

x = [23, 4, -6, 23, -9, 21, 3, -45, -8]
# Expected output
# Positive: [23, 4, 23, 21, 3] Negative: [-6, -45, -9, -8]
pos = []
neg = []

for i in range(0,9):  
  if x[i] < 0:
    neg.append(x[i])
  else:
    pos.append(x[i]) 
print(pos)
print(neg)
# new_lst = []
# new_lst.append("new name")
# print(new_lst)
# new_lst.append("RS")
# print(new_lst)