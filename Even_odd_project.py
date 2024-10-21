import time
from sty import ef,fg,rs

while True:
    try:
        name=input(f"{fg.black}Enter your name:{fg.rs} ")
        age=int(input(f"{fg.black}enter your age: {fg.rs}"))
        if age>=10 and age<=60:
            print(f"{fg.green}Loding...{fg.rs}")
            time.sleep(2)
            print(f"{fg.cyan}you can play this game.{fg.rs}")
            break
        else:
            print(f"{fg.green}Loding...{fg.rs}")
            time.sleep(2)
            print(f"{fg.copy}you can't play this game...{fg.rs}")
            print(f"{fg.cyan}age should be under (11 to 60){fg.rs}")
    except ValueError:
        print(f"{fg.green}Loding...{fg.rs}")
        time.sleep(2)
        print(f"{fg.red}invalid statement{fg.rs}")
def Even_odd(n):
    if n%2==0:
        print(f"{fg.green}Loding...{fg.rs}")
        time.sleep(2)
        print(f"{fg.cyan}number is ODD\nnumber is fuzz{fg.rs}")
    elif n%2!=0:
        print(f"{fg.green}Loding...{fg.rs}")
        time.sleep(2)
        print(f"{fg.cyan}number is EVEN\nnumber is Fizz{fg.rs}")
    else:
        print(f"{fg.green}Loding...{fg.rs}")
        time.sleep(2)
        print(f"{fg.red}please type numric values:{fg.rs} ")

n=float(input(f"{fg.black}enter value: {fg.rs}"))
# Even_odd(int(n))
while True:
    try:
        user=input(f"{fg.black}do you like to see this type (y/n) for yes or not\nType Here: {fg.rs}")
        if user.lower().strip()=="y":
            Even_odd(int(n))
            break
        elif user.lower().strip()=="n":
            print(f"{fg.green}Loding...{fg.rs}")
            time.sleep(2)
            print(f"{fg.cyan}Done!{fg.rs}")
            quit()
        else:
            print(f"{fg.green}Loding...{fg.rs}")
            time.sleep(2)
            print(f"{fg.red}Sorry{fg.rs}")
            quit()
    except ValueError:
        print(f"{fg.green}Loding...{fg.rs}")
        time.sleep(2)
        print(f"{fg.red}Error{fg.rs}")
