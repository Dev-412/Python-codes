d ={ 1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"
}
p = input("Enter roman...")
n=p
l=[]
m=[]
ans=0

for i,j in d.items():
    l.append(i)
    m.append(j)
l.reverse()
m.reverse()
    
print(l)
print(m)
while(True):
    for i in range(len(l)):
        if(n.startswith(m[i])):
            break
    ans = ans+l[i]
    print(m[i])
    if(n==p[-1]):
        break

    
    n=n[len(m[i]):999]
    
print(ans)