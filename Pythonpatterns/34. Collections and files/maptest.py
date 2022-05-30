import dis
from datetime import datetime

def sq(x):
    return x*x

# this function uses map to square every element
# and time it 1 million times
def f1():
    start = datetime.now()
    for _ in range(1000000):
        ara=[2,3,6,8,5,4]
        amap = map(sq, ara)   #map the square function
        ara1 = list(amap)
    endt = datetime.now()
    print("time=", endt-start)
    print(ara1)
    return endt-start
   
# this function squares every element of an array
# directly without using map.
# carries out the computation 1 million times and times it
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
