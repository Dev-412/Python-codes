from random import randint

class mines:
    def __init__(self,bet,n,bomb):
        if(bet<=0):
            raise Exception("Your Bet cannot Be 0 or Negative")
        if(n<=1):
            raise Exception("Minimum you should select 2x2 grid")
        if(bomb>=n*n or bomb==0):
            raise Exception("Invalid Bomb Value")
        self.bet = bet
        self.current_cash = bet
        self.n=n
        self.bomb=bomb
        self.hit=0
        self.selected=""
        self.multiplier = 1

        self.remain = (self.n*self.n)-self.bomb

    def Create(self):
        total = self.n*self.n

        self.l = [["💎"] * self.n  for i in range(self.n)]

        temp =[]
        while(len(temp)!=self.bomb):
            x = randint(0,self.n-1)
            y = randint(0,self.n-1)

            if((str(x)+str(y)) in temp):
                continue
            else:
                temp.append(str(x)+str(y))
                self.l[x][y]="💣"
        
        self.tiles=[]
        c =1
        for i in range(self.n):
            l1=[]
            for j in range(self.n):
                l1.append(c)
                c+=1
            self.tiles.append(l1)
        self.Print()

    def Play(self,z):
        if(z.upper()!="CASH" and z.isdigit()==False):
            raise Exception("Invalid Input")
        elif(z.upper()=="CASH"):
            print(f"You Cashout {self.current_cash}/-")
            return 0  
        elif(int(z)>self.n*self.n):
            raise Exception("Invalid Input")     

        z=int(z)
        z-=1
        x= z//self.n
        y= z%self.n
        a = str(x)+"+"+str(y)
        if(a in self.selected):
            raise Exception("Mine Already Selected")
        self.selected+=("."+a+".")

        if(self.l[x][y]=="💣"):
            self.tiles[x][y]=self.l[x][y]
            self.Print()
            print("You Hit A Bomb 💣...")
            print(f"You Lost {self.current_cash}/-")
            return 0
            
        elif(self.l[x][y]=="💎"):
            self.tiles[x][y]=self.l[x][y]
            self.Print()
            self.current_cash = self.update_cash()
            print(f"Current Amount = {self.current_cash}")
            if(self.remain==self.hit):
                return 0
        
    def Print(self):
        for row in self.tiles:
            print(" ".join(f"{str(col):^3}" for col in row))



    def update_cash(self):
        T = self.n * self.n          # total cells
        S = T - self.bomb            # safe cells
        # multiplier factor for THIS safe pick
        factor = (T - self.hit) / (S - self.hit)
        # update multiplier
        self.multiplier *= factor
        # update final money
        final_cash = self.bet * self.multiplier
        # increase hit AFTER calculation
        self.hit += 1
        return int(final_cash)

Bet = int(input("Enter Your Bet: "))
n = int(input("Enter Size of Board: "))
bomb = int(input("Enter Number of Bombs: "))

try:
    play = mines(Bet,n,bomb)
except Exception as e:
    print(e)
else:
    play.Create()
    while(True):
        choice = input("Select Mine/ cash to Cashout: ")
        try:
            x = play.Play(choice)
            if(x==0):
                break
        except Exception as e:
            print(e)