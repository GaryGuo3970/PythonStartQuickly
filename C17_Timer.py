import time,threading

def calcProd(i):
    product =1
    for i in range(1,i):
        product=product+1
    return product

startTime =time.time()
product = calcProd(100)
endtime=time.time()
print(f'{startTime} -  {endtime}')

#多线程
def takeNap(number):
    for i in range(1,5):
        time.sleep(1)
        print(f'Wake up {number}-{i}')

threadObj=threading.Thread(target=takeNap,args=[1])
threadObj.start()
threadObj2=threading.Thread(target=takeNap,args=[2])
threadObj2.start()

print('the end line of program')