# ---------------------------
# -------- Decorators -------
# ---------------------------

# [] Something Called Mata programming 
# [] Decorator is a higher order function (Function accepts a function as a paramter)

# Syntax of decorator Function

def mydecorator(func):
    func()
    print("hello my world befor decoration")
    print("hello my world after decoration")

@mydecorator    
def sayhello():
    print("hello mohamed")
print("#"*40)

@mydecorator
def sayhoware():
    print("how are you")
print("#"*40)

def myname():
    print("hello my name is mohamed")

print(myname())


