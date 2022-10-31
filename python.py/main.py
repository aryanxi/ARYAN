import random 
import os 
import re
from secrets import choice

from psutil import users 

os.system('cls' if os.name=='nt'else 'clear')
print("---------------------Enter the no rounds------------------------- ")
n=int(input())

def main():
 for i in range(0,n):

    print("------------------Rock,Paper,Scissors-shoot-------------------")
    userChoice= input("choose your weopean [R]ock],[P]aper],[S]cissor]:")

    if not re.match("[SsRrPp]",userChoice):
        print("MOTERFUCKER SAHI LETTER CHOOSE KARO BE:")
        print("[R]ock],[P]aper] or [S]cissor].")
        continue
    print("You choose: "+ userChoice)
    choice= ['R','P','S']
    
    opponenetChoice= random.choice(choice)
    print("i choose:"+opponenetChoice)

    if opponenetChoice==str.upper(userChoice):
        print("AARE MAIYA ...TIE")

    elif opponenetChoice=='R' and userChoice.upper()== 'S':
        print("HUM GEETE BSDK")
        continue
    elif opponenetChoice=='S' and userChoice.upper()== 'P':
        print("HUM GEETE BSDK ")
        continue
    elif opponenetChoice=='P' and userChoice.upper()== 'R':
        print("HUM GEETE BSDK ")
        continue
    else:
        print("ISS BAAR TUM GEETE BSDK ")
        
    

def hi():
    main()
    print("------------------------------THE GAME HAS BEEN ENDED---------------------------")


hi()




