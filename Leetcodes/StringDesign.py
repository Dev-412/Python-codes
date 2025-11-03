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