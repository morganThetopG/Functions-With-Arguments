#imports
import time;
import os;

#argument number
output=0

#the print function
def morg(T):
    print(str(T))
    time.sleep(0.1)
    func()

#the add and clear terminal function
def func():
    global output
    output+=1
    if output>=101:
        output=0
        os.system('cls')
    morg(output)
func()