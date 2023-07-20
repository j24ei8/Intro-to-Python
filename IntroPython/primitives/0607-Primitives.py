# Print fuction

Julie = 15


# print("Julie", 15, end="(place for new line)")
# print("Julie", 15, sep=" is ", end="(place for new line)")
# print("Julie", 15, sep=" #* ")
# print("Julie", 15, "Julie", 15, sep=" is ", "Julie", 15, sep=" #* ")
# print("Julie 15", "Julie is 15", "Julie #* 15")

# print("Rosalyn", 30)



# Data Type

# 1) String
# ex) " ", ".", "Julie", "15" "a;lskdfj;laksjdf"
# 2) integer
# ex) -10000, 999, 40
# 3) floats
# ex) 3.14, 8.8888, 457.6666, e, pi, 1/4
# 4) boolean
# ex) True (1), False (0)


# Operations
# 1) Additions +
print(5+10)
print("5"+"10")
print("5+10")
# 2) Subtraction -
print(100000-1)
# print("100000"-"1")
# 3) Division /
print(10/3)
# 3-1) // (dividend)
print(10//7)
# 3-2) % (modulo;mod;remainder)
print(10%7)

# 4) Multiplication *
print(5*10)
# print("5"*"10")
print("5"*10)
print(5*"10")
print(5*"JULIE!!!!")
print("5*10")

# inequalities
# 1) greater than --> a > b
# 2) less than --> a < b
# 3) greater than equal to --> a >= b
# 4) less than equal to --> a <= b

# If statement
Julie = 19
if Julie < 19:
  print("Julie is under 19")
  print("So she can't drink")
print("Julie is or over 19")
print("So she can drink")


a=50
b=60
# 1) First Type
if a < b:
  print("a is less than b")
elif a > b:
  print("b is less than a")
else:
  print ("they are equal")

# 2) Second Type
if a < b: print("a is less than b")

# 3) Third Type
print("a is less than b") if a < b else print ("they are equal")


# find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).

num = 175

if num%7==0 and num%5==0:
  print(num, "is divisible by 7 and 5")
elif num%7==0:
  print(num, "is divisible by 7")
elif num%5==0:
  print(num, "is divisable by 5")
elif 1500 < num and num < 2700: 
  print (num, "between 1500 and 2700")
else:
  print ("not applicable")




