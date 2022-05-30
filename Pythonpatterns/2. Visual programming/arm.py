import time
import dis

""""List comprehension"""

def comprehend():
    for _ in range(1000000):
        squares = [value**2 for value in range (1,21)]
        

#print(squares)

#equivalent code

def fularray():
    for _ in range(1000000):
        squares = [value**2 for value in range(1,21)]
   
#print (squares)

#conditional comprehension
#nlist = [x for x in range(20) if x%2==0]
#print (nlist)

#start here
stime = time.monotonic()
comprehend()
etime=time.monotonic()
print(etime- stime)

stime = time.monotonic()
fularray()
etime=time.monotonic()
print(etime- stime)     

dis.dis(comprehend())

dis.dis(fularray())


