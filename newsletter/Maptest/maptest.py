import dis
from datetime import datetime

def sq(x):
    return x*x

def f1():
    start = datetime.now()
    for _ in range(1000000):
        ara=[2,3,6,8,5,4]
        amap = map(sq, ara)
        ara1 = list(amap)
    endt = datetime.now()
    print("time=", endt-start)
    print(ara1)
    return endt-start
   
        
def f2():
    start = datetime.now()
    ara=[2,3,6,8,5,4]

    for _ in range(1000000):
        amap = [sq(a) for a in ara]
    endt = datetime.now()
    print("time=", endt-start)
    return endt-start
       
t1 = f1()
t2 = f2()
print (t1,t2, (t2-t1)/t2)
#dis.dis(f1)
