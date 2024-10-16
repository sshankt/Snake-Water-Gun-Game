import random 
import pyttsx3
engine = pyttsx3.init()
print(".............................................")
print("Welcome to the Water Snake Gun game 2.0")
engine.say("Welcome to the Water Snake Gun game 2.0")
engine.runAndWait()
print("..............................................")
print("Enter..........\n s. snake\nw.  water\ng.  gun")


while True:
    computer= random.randint(-1, 1) 

    youstr = input("Enter your choice :")
    youDict = {"s": 1 , "w" : -1 , "g" :0}
    reverseDict = {1 :"snake", -1 : "water", 0 : "Gun"} 
    you = youDict[youstr] 
    print(f"You choose {reverseDict[you]}\n Computer choose {reverseDict[computer]}") 
    if(you == computer):
        print("Its Draw !")
    elif(computer == -1 and you == 1):
        print("You win !") 
    elif(computer == -1 and you == 0):
        print("You Lose !")
    elif(computer == 1 and you == -1):
        print("You Lose !") 
    elif(computer == 1 and you == 0):
        print("You Wins !")
    elif(computer == 0 and you == 1):
        print("You Lose !")
    else :
        print("You Went Wrong !")
        print("Please Try Again :") 


# Its the second way to make a game in less line of code 

""" if((computer - you) == -1 or (computer - you) == 2):
    print("You Lose !")
else:
    print("You Wins !") 
 """