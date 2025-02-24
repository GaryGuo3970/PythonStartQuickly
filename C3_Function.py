#1
def Hello(name):
    print('hello:'+name)

Hello('Gary')

#2
def Add(a:int,b:int):
    c:int
    c=10000
    #全局变量，局部变量
    return a+b+c+d

d:int
d=1000

print(Add(1,11))

#3
def GlobalVar():
    global eggs
    eggs = "global variable"

GlobalVar()
Hello(eggs)

#4 exception
def TryFun(a,b):
    try:
        print(a/b)
    except:
        print("有异常!")

TryFun(10,3)
TryFun(10,0)