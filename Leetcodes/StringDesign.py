
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