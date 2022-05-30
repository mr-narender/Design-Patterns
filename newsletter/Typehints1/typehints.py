""" Illustration of type hints """
def adder(x:float, s:str) -> float:
    return x + float(s)

def adder(x: float, y: float) -> float:
    return x + y

result: float = adder(2, "3")
print(result)
result = adder(1, 2)
print(result)
