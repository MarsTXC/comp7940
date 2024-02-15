import json
import requests

site = "https://api.npoint.io/2b57052af2060e84dc86"

# Function to convert all elements (except the first one) into numbers and return as a list
def convert_number(data):
    return [int(item) for item in data[1:]]
    
# Function to replace all occurrences of 'being_replace' with 'to_replace'
def replace_number(number_list, being_replace, to_replace):
    return [to_replace if item == being_replace else int(item) for item in number_list]

# Trying to load JSON into text
r = requests.get(site)
data = r.json()['users']

# Debug
for i in data:
    print("parse " + str(i))

# Call the function convert_number
# Convert all elements (except the first one) into numbers and return it as a list
y = convert_number(data[0])
print("y")
print(y)

# Call the function replace_number
# Replace all occurrences of 1 by the number 10 in the function
z = replace_number(number_list=y, being_replace=1, to_replace=10)
print("z")
print(z)

# Calculate the sum
sum_result = 0
for i in z:
    sum_result += i
    print("sum = " + str(sum_result) + "; i = " + str(i))
print("Total = " + str(sum_result))
