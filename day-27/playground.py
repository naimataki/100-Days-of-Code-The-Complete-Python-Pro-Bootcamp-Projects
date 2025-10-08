# Unlimited Postional arguments
def add(*args):
    print(args[1])

    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1, 2, 3, 7, 8, 9, 20, 21, 33))

#def calculate(**kwargs):
