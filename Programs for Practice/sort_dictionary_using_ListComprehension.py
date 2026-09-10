# d1={575:"Mango",133:"kivi", 120:"grapes", 576:"Banana"}
# d2={key:value for key,value in sorted (d1.items(),key=lambda x:x[1])}
# print(d2)


# 0R


d1={
    10:'mango',20:'grapes',30:'coconut',50:'leach',25:'Dragon-fruit',28:'pinapple'
}
e=sorted(d1.keys())

d2={}

for i in e:
    d2[i]=d1[i]
print(d2)
