import random

print(random.randint(0,100))

def roomResult(x:int=5):
    # less than 20.  Dead
    
    return random.randint(0,100) >= 20 + x

x = "this is a variable in a 500 line long file i forgot about."
for _ in range(100):
    print(roomResult())
    
for _ in range(100):
    print(roomResult(34))
    
def sayHigh(to:str="me", from:str="you"):
    #print("hi")
    return(f"hi from {from} to {to}")
    
print(sayHigh())
    