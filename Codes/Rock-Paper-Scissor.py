from random import randint

class game:
    def __init__(self):
        self.S_player =0
        self.S_computer =0

    def play(self,choice):
        x = randint(1,3)
        if(x==1):
            computer="ROCK"
        elif(x==2):
            computer="PAPER"
        else:
            computer="SCISSOR"

        choice=choice.upper()

        print("------------------------------")
        if(choice==computer):
            print(f"You Chose = {choice} Computer Chose = {computer}")
            print("Its a Draw!!!")

        elif(choice=="ROCK" and computer=="PAPER"):
            print(f"You Chose = {choice} Computer Chose = {computer}")
            self.S_computer =self.S_computer+1
            print("You Lost!!!")

        elif(choice=="ROCK" and computer=="SCISSOR"):
            print(f"You Chose = {choice} Computer Chose = {computer}")
            self.S_player=self.S_player+1
            print("You Wonn!!!")

        elif(choice=="PAPER" and computer=="ROCK"):
            print(f"You Chose = {choice} Computer Chose = {computer}")
            self.S_player=self.S_player+1
            print("You Wonn!!!")

        elif(choice=="PAPER" and computer=="SCISSOR"):
            print(f"You Chose = {choice} Computer Chose = {computer}")
            self.S_computer =self.S_computer+1
            print("You Lost!!!")

        elif(choice=="SCISSOR" and computer=="ROCK"):
            print(f"You Chose = {choice} Computer Chose = {computer}")
            self.S_computer =self.S_computer+1
            print("You Lost!!!")

        elif(choice=="SCISSOR" and computer=="PAPER"):
            print(f"You Chose = {choice} Computer Chose = {computer}")
            self.S_player=self.S_player+1
            print("You Wonn!!!")
        else:
            print("INVALID_CHOICE!!!")
        print("------------------------------")
        print("----------Score-card----------")
        print(f"Your Score: {self.S_player}")
        print(f"Computer Score: {self.S_computer}")
        print("------------------------------")

obj = game()
while(True):
    x = input("Enter Choice / Exit to Quit: ")

    if(x.upper()=="EXIT"):
        print("Thanks For Playing")
        break
    else:
        obj.play(x)
