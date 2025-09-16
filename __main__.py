from InquirerPy import inquirer
from InquirerPy import get_style
import sys
import os

import play

def main():
    os.system("cls")
    menuMain()
    #menuPlay()

def menuMain():
    choice = inquirer.select(
        message="BadApple.py",
        choices=["Play", "Sampling", "Exit"],
        instruction="↑↓ Move, Enter Select",
        qmark="🍎",
        style=get_style({
            "question": "fg:#ff6347 bold",
            "instruction": "#5f5f5f",
            "pointer": "#61afef"
        })
    ).execute()
    os.system("cls")

    if choice == "Exit":
        sys.exit()
    elif choice == "Play":
        menuPlay()
        return
    elif choice == "Sampling":
        print("Comming Soon")
        return

def menuPlay():
    choice = inquirer.select(
        message="Select File To Play",
        choices=(lambda _:
            [f for f in os.listdir("./sampling/") if f.endswith(".json")] + ["Back"]
        ),
        instruction="↑↓ Move, Enter Select",
        qmark="🍎",
        style=get_style({
            "question": "fg:#FF9147 bold",
            "instruction": "#5f5f5f",
            "pointer": "#61afef"
        })
    ).execute()
    os.system("cls")

    if choice == "Back":
        menuMain()
        return

    print(choice)
    play.playBadApple(choice)

if __name__ == "__main__":
    main()
