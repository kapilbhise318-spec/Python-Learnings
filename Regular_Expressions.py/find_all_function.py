# re.findall()

# Returns all matching values as a list.


import re

text = "My numbers are 123 and 456"

result = re.findall("\d+", text)

print(result)