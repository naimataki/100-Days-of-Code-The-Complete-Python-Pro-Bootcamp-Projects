def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

sum = add (1 + 2 + 3 + 7 + 8 + 9 + 20 + 21 + 33)
print(sum)