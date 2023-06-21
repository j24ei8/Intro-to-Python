# Write a Python script to concatenate the following dictionaries to create a new one.

# Sample Dictionary : 
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

result = {}

for key, value in dic1.items():
  result[key]=value 
for key, value in dic2.items():
  result[key]=value 
for key, value in dic3.items():
  result[key]=value 
print (result)
  
