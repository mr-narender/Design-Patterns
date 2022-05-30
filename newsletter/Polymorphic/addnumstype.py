""" This is a revised version of this class.
Actually Python does not allow multiple methods with the same name
since it uses a one-pass compiler. So the intended polymorphism doesn't actually work.

This example uses the type function to dispatch addNums(f,f) to addNumsF
"""

class Summer():
    def addNumsf(self, x: float, y: float) ->float:
        return x + y

    def addNums(self, f: float, s: str) -> float:
        return self.addNumsf(f,s) if type(s) is float else f + float(s)

#----------------------------------
def main():
    sumr = Summer()
    print(sumr.addNums(12.0, 2.3))
    print(sumr.addNums(22.3, "13.5"))
    # This will fail
   # val = sumr.addNums('22.3', '13.5')
    #print(val)

###  Here we go  ####
if __name__== "__main__":
    main()