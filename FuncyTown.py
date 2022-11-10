#imports
import time;
import os;

#argument number
list=[]
total=0
#the print function
def morg(T):
    print(str(T))
    time.sleep(0.1)
    func()

#the add and clear terminal function
def func():
    global total
    usr=float(input("GIVE A NUMBER: "))
    total=total+usr
    list.append(usr)
    print("\n"+str(list)+"\n")
    ext=input("Add All Numbers? Y/N: ")
    if ext=="y":
        morg(total)
    else:
        func()
func()
