# import re

# text="Hello World"

# print(re.search(r"World",text))
# print(re.match(r"World",text))
# print(re.match(r"Hello",text))


# import re
# match=re.search(r"\d+","Room 42")
# if match:
#     print(match.group())


# re.findall()
# import re
# text="Call 123-456-7890 or 987-654-3210"
# print((re.findall(r"\d{3}-\d{3}-\d{4}",text)))


# import re
# text="Guiddow Van Rossum Was the Founder Of Python"
# print(re.match("Guiddow",text))
# print(re.search("Founder",text))





# 2)... Modifiers..

# I= INGORECASE(re.I)


# import re
# text="hello"
# print(re.search("Hello",text,re.I))


# text1="Guiddow \nVan Rossum"
# print(re.search("^Guiddow",text1,re.M))

# import re
# text2="Java\nRollins"
# print(re.search("Java.*Rollins",text2, re.S))





# import re

# text = "Hello\nWorld"
# print(re.search("Hello.*World", text, re.S))



# PATTERN

import re
pattern="complexity"
text="understanding language Ruby is quite complexity"
p1=(re.search(pattern,text))
print(p1.group())