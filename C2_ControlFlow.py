import random

def printHelloWorld():
    isEqual ='Hello' =="Hello"
    print(isEqual)
    youName=input()
    if(youName=="Gary"):
        print("欢迎您："+youName)
    else:
        print("不欢迎你："+youName)
    i=0
    while i<5:
        print(i)
        i=i+1
    print("for")
    for i in range(10,100,2):
        print(i)
    print("for-")
    for i in range(10,-1,-1):
        print(i)

def randmoFun():
    for i in range(10):
        print(random.randint(1,100))

def GuessNumber():
    import random,sys
    print('石头,    布,  剪刀')
    wins=0
    losses=0
    ties=0
    while True:
        print('%s wins, %s losses, %s ties'%(wins,losses,ties))
        while True:
            print('输入你的动作：（r) 石头 (p) 布 (s) 剪刀 or (q) 退出')
            playerMove=input()
            if(playerMove=='q'):
                sys.exit()
            if(playerMove == 'r' or playerMove=='p' or playerMove=='s'):
                break
        if(playerMove=='r'):
            print("     石头 vs ")
        if(playerMove=="p"):
            print("     布 vs")
        if(playerMove=='s'):
            print("     剪刀 vs")

        randNumber=random.randint(1,3)
        if(randNumber==1):
            computerMove='r'
            print("     石头")
        if(randNumber==2):
            computerMove='p'  
            print("     布")      
        if(randNumber==3):
            computerMove='s'
            print("     剪刀")

        if playerMove==computerMove:
            print("平局！")
            ties=ties+1   
        # r 石头 p 布 s 剪刀
        elif playerMove=='r' and computerMove=='p':
            print("电脑赢！")
            losses=losses+1     
        elif playerMove=='r' and computerMove=='s':
            print("玩家赢！")
            wins=wins+1     
        elif playerMove=='p' and computerMove=='r':
            print("玩家赢！")
            wins=wins+1
        elif playerMove=='p' and computerMove=='s':
            print("电脑赢！")
            losses=losses+1
        elif playerMove=='s' and computerMove=='r':
            print("电脑赢！")
            losses=losses+1
        elif playerMove=='s' and computerMove=='p':
            print("玩家赢！")                        
            wins=wins+1    
if __name__ == "__main__":
    # printHelloWorld()
    # randmoFun()
    GuessNumber()