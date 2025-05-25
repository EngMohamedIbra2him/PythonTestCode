# -------------------------------------------------------------------
# ---------------- Decorators - Function With Parameters ------------
# -------------------------------------------------------------------

# def odoodecorate(func):
#     def nestedfunction(num1,num2):
#         print("hello world befor odoo")
#         func(num1,num2)
#         print("hello world after odoo")
#     return nestedfunction


# @odoodecorate
# def dodoo(n1,n2):
#         print(n1+n2)

# # print(dodoo(10,20))

def odoodecorate(func):                     # unlimited Argument
    def nestedfunction(*num):
        print("hello world befor odoo")
        func(*num)
        print("hello world after odoo")
    return nestedfunction

@odoodecorate
def calculated(n1,n2,n3,n4):
    print(n1+n2+n3+n4)

calculated(10,20,30,40)