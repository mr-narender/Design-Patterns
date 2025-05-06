"""Some simple functions"""
# return a square of the input value
def sqr(x):
    return x * x

def cube(a):
    return sqr(a) * a

"""main program begins here"""
def main():
    xvar = 12
    print(xvar, sqr(xvar), cube(xvar))

###  This is the real entry point ####
if __name__ == "__main__":
    main()                  #call main() here
