def d():
    animal = "elephant"

    def e():
        nonlocal animal
        animal = "penguin"
        print("inside nested function:", animal)
    print("Before calling function:", animal)
    e()
    print("After calling function:", animal)


animal = "gator"
d()
print("Global variable: ", animal)
