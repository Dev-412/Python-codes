days = int(input("enter no of days"))

w = days//7
d = days%7

sum1=0
temp=1

for i in range(w):
    temp2=temp
    for j in range(7):
        sum1=sum1+temp2
        temp2+=1
    temp+=1

for i in range(d):
    sum1+=temp
    temp+=1

print(f"Total money gathered ={sum1}")