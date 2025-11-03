x ="good morning"

y = x.split(" ")
y="".join(y)

bottom=0

triple=[]
single=[]
flag =False

while bottom<len(y):
    
    for j in range(3):
        triple.append(y[bottom])
        if(bottom==len(y)-1):
            flag=True
            break
        bottom=bottom+1

    if(flag==True):
         break

    if(bottom==len(y)):
            break

    single.append(y[bottom])
    bottom=bottom+1
    
    
print(triple)
print(single)


print(triple[::3]+[" ",])
print(triple[1::3]+[" ",])
print(triple[2::3]+[" ",])

a=triple[::3]
a=" ".join(a)
print(a)

temp=0
for i in(triple[1::3]):
    print(i,end="")
    if(temp==len(single)):
         continue
    print(single[temp],end="")
    temp=temp+1
print("")

c=triple[2::3]
c=" ".join(c)
print(c)










# 2nd methodddd

x= "goodmorning"
y=x[3::4]
a=0
for i in (x[::4]):
    print(i,end="")
    if(a==len(x[::4])-1):
        break
    print(" ",end="")
    a=a+1
print("")
a=0
for i in (x[1::4]):
    print(i,end="")
    if(a==len(x[::4])-1):
        break
    print(y[a],end="")
    a=a+1
print("")
a=0
for i in (x[2::4]):
    print(i,end="")
    if(a==len(x[::4])-1):
        break
    print(" ",end="")
    a=a+1