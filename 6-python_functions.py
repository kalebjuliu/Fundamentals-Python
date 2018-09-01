
def functionName(x,y):
    num =  x + y
    print("the answer is",num)
functionName(1,3)



def defaultParam(num1, num2 = 5):
    print(num1,num2)
defaultParam(5)


def basicWindow(width,height,font="tnr",
                bgc="w"):
    print(width,height,font,bgc)

basicWindow(500,300)
basicWindow(500,300, bgc="b")
#changing default parameter by typing the specific parameter
                              
