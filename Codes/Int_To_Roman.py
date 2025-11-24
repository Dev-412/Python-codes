d ={ 1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"
}
n = int(input("Enter number..."))
l=[]
m=[]
ans=""

for i,j in d.items():
    l.append(i)
    m.append(j)
    
while(n!=0):
    for i in range(len(l)):
        if(l[i+1]>n or l[i]==n):
            break
    ans = ans+m[i]
    n=n-l[i]
    
print(ans)