Write a Python program to map two lists into a dictionary.

Sample Solution:-

Python Code:

keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
color_dictionary = dict(zip(keys, values))
print(color_dictionary)