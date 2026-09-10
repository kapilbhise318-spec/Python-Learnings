# A lambda function is small annymsfunction(a function withou name) 
# it is mainly used for short and simple operations...
# lambda is commonly used map(), filter(), and sorted()


# Add two numbers
add=lambda a,b:a+b
print(add(10,20))

# square of a number
square=lambda x: x*x
print(square(5))

# Lambda with map() function

nums=[1,2,3,4]

result=list(map(lambda x: x * 2, nums))
print(result)


# Lambda with filter() function
n=[1,2,3,4,5,6,7,8,10]

even=list(filter(lambda x: x%2 ==0, n))
print(even)


# Lambda with sorted() function
data={
    101:'Kapil',
    102:'Harry',
    103:'Sharda',
    104:'sam'
}

result=sorted(data.items(), key=lambda x:x[1])
print(result)