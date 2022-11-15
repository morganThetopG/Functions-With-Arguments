def myfunction(x1,x2,x3):
    return x1+x2+x3


arglist = [1,2,3,4,5,6,7,8,9]
for _ in range(3):
    print(myfunction(arglist[_+0],arglist[_+1],arglist[_+2]))
    #remove used arguments from the list 
    arglist= arglist[2:] 
