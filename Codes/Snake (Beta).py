from random import randint
import msvcrt
import time
import os

class snake_game:
    def __init__(self,n):
        self.grid = []
        self.snake = []
        self.head = ()
        self.n=n
        self.food= None

        
    def create(self):

        self.grid = [["." for i in range(self.n)] for i in range(self.n)]
        mid = self.n // 2
        self.snake = [(mid, mid), (mid, mid-1), (mid, mid-2)]
        self.head = self.snake[0]
        for i in self.snake:
            x = i[0]
            y = i[1]
            if i == self.head:
                self.grid[x][y]="H"
            else:
                self.grid[x][y]="O"
        food = self.Spawn_food()
        self.grid[food[0]][food[1]]="F"
        # print("\033[?25l", end="")

    def movement(self,z):
        # valid input check 
        check = ".w.W.s.S.a.A.d.D"
        if (z in check):
            pass
        else:
            raise Exception("Invalid Input")
    
        d = {"W":(-1,0),"S":(1,0),"A":(0,-1),"D":(0,1)}
        temp = d[z.upper()]
        change_x = temp[0]  # change in x coord
        change_y = temp[1]  # change in y coord

        temp2 = self.snake[0]

        new_x=temp2[0]+change_x #next x coord
        new_y=temp2[1]+change_y #next y coord
        if(len(self.snake) > 1 and (new_x,new_y)==self.snake[1]): #self collision
            return 1
        elif(new_x==-1 or new_y==-1 or new_x==self.n or new_y==self.n): #border collision
            return 1
        elif((new_x,new_y) in self.snake): #self collision
            return 1
        elif((new_x,new_y)==self.food):
            self.snake.insert(0,(new_x,new_y))
            self.head = self.snake[0]
            self.food=None
        else:
            self.snake.insert(0,(new_x,new_y))  #add new location
            self.snake.pop() #remove last location to move
            self.head = self.snake[0]

        #rewrite whole board with new snake location
        self.grid = [["." for i in range(self.n)] for i in range(self.n)]
        for i in self.snake:
            x = i[0]
            y = i[1]
            if i == self.head:
                self.grid[x][y]="H"
            else:
                self.grid[x][y]="O"
        food1 = self.food
        if(food1==None):
            food1 = self.Spawn_food()
        self.grid[food1[0]][food1[1]]="F"
        # print("\033[H", end="")
        self.clear_screen()
        self.Print()

    def Spawn_food(self):

        total = self.n*self.n
        snake = len(self.snake)
        remaining_space = total-snake
        
        if(remaining_space==0):
            self.food = None
            return

        while(True):
            x = randint(0,self.n-1)
            y = randint(0,self.n-1)

            if((x,y) in self.snake):
                continue
            else:
                break

        self.food = (x,y)
        return self.food


    def Print(self):
        for i in self.grid:
            for j in i:
                print(j,end=" ")
            print()
    
    def clear_screen(self):
        os.system("cls")


direction = "right"
n = int(input("Enter Size of Board"))
x = snake_game(n)
x.create()
key=None
last_tick_time = time.monotonic()
tick=0.250
while(True):
    
    if(msvcrt.kbhit()):
        key = msvcrt.getch().decode()
        check = ".w.W.s.S.a.A.d.D."
        d={"w":"top","s":"bottom","a":"left","d":"right"}
        if key in check:
            direction = d[key]
        else:
            key=None


    now = time.monotonic()
    if(now-last_tick_time>=tick):

        try:
            if(key==None):
                d1={"top":"w","bottom":"s","left":"a","right":"d"}
                z = x.movement(d1[direction])
                if(z==1):
                    print("Collision!! You Lost..")
                    break
            else:
                z = x.movement(key)
                key=None
                if(z==1):
                    print("Collision!! You Lost..")
                    break
            last_tick_time = now
        except Exception as e:
            print(e)
