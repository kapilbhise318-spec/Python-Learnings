# Search number/element in the list


# list=[10,20,3,40,50,44]

# search_element=int(input("Enter a number to search in the list: "))

# if search_element in list:
#     print(search_element, "-The number is present in the list..")
# else:
#     print(search_element, "-The number is not presentt in the list")


# # 






# Find the index number of element in the list

numbers=[12,34,56,78,99]

find_index=int(input("Enter an element to findout it index number: "))

if find_index in numbers:
    print("Entered element is", find_index, "and its index number is ",numbers.index(find_index))
else:
    print("Element is not present in the list")
