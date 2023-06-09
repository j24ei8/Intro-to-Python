Julie = 15
while Julie > 19:
  print("Julie")


# guess a number between 1 and 9.
num = 5
guess = int(input("Guess a number 1 through 9:"))
while num != guess:
  
  if guess > num: 
    print ("guess is greater than num")
  elif guess < num:
    print ("guess is less than num")
    
  guess = int(input("Guess a number 1 through 9:"))
  
print ("guess is correct")
