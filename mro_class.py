class A:
    num = 10
class B(A):
    num = 20

class C(B):
    pass
print(C.help())