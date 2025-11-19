#FileNotFoundError
#with open("a_file.txt") as file:
#    file.read()

try:
    file = open("day-30/a_file.txt")
except:
    open("day-30/a_file.txt", "w")
    #print("There was an error")

#KeyError
#a_dictionary = {"key": "value"}
#value = a_dictionary["non_existent_key"]

#IndexError
#fruit_list = ["Apple", "Banana", "Pear"]
#fruit = fruit_list[3]

#TypeError
#text = "abc"
#print(text + 5)