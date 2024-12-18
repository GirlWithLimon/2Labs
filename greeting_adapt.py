#!/home/vboxuser/PycharmProjects/pythonProject/.venv/bin/python
import sys
def with_file(arg: list[str]):
    with open(arg[1],"r") as f:
        for line in f:
            string=line.strip()
            if not string:
                continue
            if string[0].islower():
                sys.stderr.write(f"Error! Name {string} with a small first letter\n")
            elif not string.isalpha():
                sys.stderr.write(f"Error! Name {string} does not consist only of letters\n")
            else:
                print(f"Nice to see you, {string}!")

def without_file():
   try:
       while True:
           A=input("Hello! What is your name? ")
           if A[0].islower():
               print(f"Name {A} with a small first letter")
           elif not A.isalpha():
               print(f"Name {A} does not consist only of letters")
           else:
               print(f"Nice to see you, {A}!")
   except KeyboardInterrupt:
        print("\nGoodbye!")
sys.stderr=open('errors.txt','w')
if len(sys.argv)>1:
    filename=sys.argv[1]
    if filename.endswith(".txt"):
        namefile=sys.argv
        with_file(namefile)
    else:
        print(f"You must specify the format .txt for file. If the input without a file, make only a program call")
else:
    without_file()

