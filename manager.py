import os
from CommandParser import parse
# run the user's program in our generated folders
os.chdir('module/root_folder')


# put your code here

def gui():
        if 'logs.txt' in os.listdir():
            os.remove('logs.txt')
        while(True):
            user_input = input("")
            output = parse(user_input)
            if output == None:
                return
            else:
                print(output)

def test():
    print("it's Working")

def main():
    gui()
if __name__ == '__main__':
    main()





