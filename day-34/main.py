#age: int
#name: str
#height: float
#is_human: bool

#age = 12 #can't be a string or any other datatype instead

def police_check(age: int) -> bool: #type hint
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

print(police_check(12))

if police_check(19):
    print("You may pass")
else:
    print("Pay a fine")


