#file = open("day-24/my_file.txt") 
#contents = file.read()
#print(contents)
#file.close()

#read a file
#with open("day-24/my_file.txt") as file:
#    contents = file.read()
#    print(contents)

#write in a file
with open("day-24/my_file.txt", mode="a") as file:
    file.write("\nNew text.")

#create and write in a new file
with open("day-24/new_file.txt", mode="w") as file:
    file.write("\nNew text.")