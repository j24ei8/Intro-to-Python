lst1=["Joe", "Sarah", "Mike", "Jess", "", "Matt", "", "Greg"]
lst2=[]

# Program a while loop that stops when it encounters an emtpy string ("")

# for i in range(0,8):  
#   if lst1[i] != "":
#     print(lst1[i])
#   else:
#     break
  
# for i in range(0,8):  
#   if lst1[i] != "":
#     print(lst1[i])
#   else:
#     continue 

# i=0
# while lst1[i] != "":
#   print(lst1[i])
#   i = i+1

# i=0
# while True:
#   print(lst1[i])
#   i = i+1
#   if lst1[i] == "":
#     break 

i=0
while True:
  print(lst1[i])
  i = i+1
  if lst1[i] == "":
    continue 