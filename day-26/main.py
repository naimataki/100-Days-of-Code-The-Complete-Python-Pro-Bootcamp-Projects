#list = [i*2 for i in range(1,5)]
#print(list)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)