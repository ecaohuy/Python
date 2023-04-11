# Example 1
class A:
   def a(self):
       return "Function inside A"

class B:
    def a(self):
        return "Function inside B"

class C(B,A):
    pass

# Driver code
c = C()
print(c.a())


value = 7
class A:
    value = 5

a = A()
a.value = 3
print(value)


bravo = 3
b = B()
class B:
    bravo = 5
    print("Inside class B")
c = B()
print(b.bravo)