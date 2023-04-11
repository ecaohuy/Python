def d():
    animal = "elephant"
    def e():
        nonlocal animal
        animal = "giraffe"
        print("Inside e():", animal)

    print("Before calling e():", animal)
    e()
    print("After calling e():", animal)
animal = "camel"
d()
print("Global:", animal)