class conversion:  
    def StringToBinary(self,String):
        Binary=""
        for i in String:
            temp=ord(i)
            temp = str(format(temp,'08b'))
            Binary+=temp
        return(Binary)

    def BinaryToString(self,Binary):
        String=""
        start=0
        end=8
        for i in range(len(Binary)//8):
            temp = Binary[start:end]
            start+=8
            end+=8
            temp = int(temp,2)
            String+=chr(temp)
        return(String)

s = conversion()
x = "my name is dev 1234 hahahah"
y = s.StringToBinary(x)
print(y)

print(s.BinaryToString(y))
