#3.1: Names.
names = ["Jul", "Del", "Joe Noeske", "Mr.Carter"]

i = 0
while i < len(names):
    print(names[i])
    i = i + 1


#3.2: Greetings.
names = ["Jul", "Joe Noeske", "Mr.Carter"]

print(f"Hey {names[0]}, be strong bud.")
print(f"Good morning {names[1]}, you are the best mentor I could ever ask for.")
print(f"{names[2]}, I will be honest. You are like a father to me.")

#3.3: Your Own List.
vehicle = ["One Wheel", "M1A2 Abram", "Ka-52"]
i = 0
while i < len(vehicle):
    print(f"I would like to own a/an {vehicle[i]} one day!")
    i = i + 1
    
#3.4: Guest List.
invite = ["Deus", "Paul", "Steve Jobs", "Elon Musk"]

i = 0
while i < len(invite):
    print(f"{invite[i]}, please come to my party!!!")
    i = i + 1

#3.5: Changing Guest List.
invite = ["Deus", "Paul", "Steve Jobs", "Elon Musk"]

i = 0

print(f"{invite[2]} cannot make it to the party :<")

del invite[2]

invite.append("Harry")


while i < len(invite):
    print(f"{invite[i]}, please come to my party!!!")
    i = i + 1
    
#3.6: More Guests.
invite = ["Deus", "Paul", "Steve", "Elon"]

i = 0

print(f"{invite[2]} cannot make it to the party :<")

del invite[2]

invite.append("Harry")


while i < len(invite):
    print(f"{invite[i]}, please come to my party!!!")
    i = i + 1
    
print("I found a bigger table")

invite.insert(0, "Gary")
invite.insert(2, "Joe")
invite.append("Michael")

n = 0

while n < len(invite):
    print(f"Hey {invite[n]}, please join the dinner!")
    n = n + 1
    
#3.7: Shrinking Guest List.
invite = ["Deus", "Paul", "Steve", "Elon"]

i = 0

print(f"{invite[2]} cannot make it to the party :<")

del invite[2]

invite.append("Harry")


while i < len(invite):
    print(f"{invite[i]}, please come to my party!!!")
    i = i + 1
    
print("I found a bigger table")

invite.insert(0, "Gary")
invite.insert(2, "Joe")
invite.append("Michael")

n = 0

while n < len(invite):
    print(f"Hey {invite[n]}, please join the dinner!")
    n = n + 1
    
print("\n Woops, I can only invite two people now. Sorry guys!")

first_remove = invite.pop(6)
print(f"Sorry {first_remove.title()}, but the dinner is full so you won't be able to join.")
second_remove = invite.pop(5)
print(f"Sorry {second_remove.title()}, but the dinner is full so you won't be able to join.")
third_remove = invite.pop(4)
print(f"Sorry {third_remove.title()}, but the dinner is full so you won't be able to join.")
forth_remove = invite.pop(3)
print(f"Sorry {forth_remove.title()}, but the dinner is full so you won't be able to join.")
fifth_remove = invite.pop(2)
print(f"Sorry {fifth_remove.title()}, but the dinner is full so you won't be able to join.")

print(f"Dear {invite[0]} and {invite[1]}, you both are still invited to the dinner!")

del invite[1]
del invite[0]

print(invite)

#3.8: Seeing the world.
places = ["Paris", "London", "Da Lat", "Seoul", "Hokkaido", "D.C", "Canada"]
print("This is the original list: ")
print(places)

print("\nThis is the list but in order: ")
print(sorted(places))

print("\nThis is the orginal list again: ")
print(places)

print("\nThis is the list but in reversed order: ")
print(sorted(places, reverse=True))

print("\nThis is the original list: ")
print(places)

print("\nThis is the list in reversed order: ")
places.reverse()
print(places)

print("\nThis is the original list: ")
places.reverse()
print(places)

print("\nThis is the list in order: ")
places.sort()
print(places)

print("\nThis is the list in revered order: ")
places.sort(reverse=True)
print(places)

#3.9: Dinner Guests.


#3.10: Every Function.
learn = ["Python", "Kali", "OpenCV", "Raspberry Pi", "Networking", "GitHub"]

print(learn)

print(len(learn))

print(learn[4])

print(learn[-4])

learn[0] = "Penetration Testing"
print(learn)

learn.append("Cryptography")
print(learn)

learn.insert(0, "Python")
print(learn)

del learn[3]
print(learn)

most = learn.pop(1)
print(f"What I want to learn the most right now is {most}!")

learn.remove("Raspberry Pi")
print(learn)

learn.sort()
print(learn)

learn.sort(reverse = True)
print(learn)

learn.reverse()
print(learn)

#3.11: Intentional Error.
