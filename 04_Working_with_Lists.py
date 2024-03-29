#4.1: Pizzas.
type_of_pizza = ["Hawaiian", "Seafood", "Greek"]

for pizza in type_of_pizza:
    print(f"I love {pizza} pizza!!!")

print("I really love pizza!")

#4.2: Animals.
pets = ["British short hair", "Golden Retriever", "Pug"]

for pet in pets:
    print(f"I would love to have a {pet} as a pet!")

print("All of them would make great pet!!!")

#4.3: Counting to Twenty.
number = list(range(0,21))

for num in number:
    print(num)

#4.4: One Million.
number = list(range(0,1000001))

for num in number:
    print(num)

#4.5: Summing a Million.
number = list(range(0,1000001))

print(min(number))
print(max(number))
print(sum(number))

#4.6: Odd Numbers.
odd = list(range(1,21,2))

for number in odd:
    print(number)

#4.7: Threes.
odd = list(range(3,31,3))

for number in odd:
    print(number)

#4.8: Cubes.
cubes = []

for number in range(1,11):
    cube = number ** 3
    cubes.append(cube)
    
for cube_num in cubes:
    print(cube_num)

#4.9: Cube Comprehension.
cubes = [cube**3 for cube in range(1,11)] 
print(cubes)

#4.10: Slices.
cubes = [cube**3 for cube in range(1,11)]
print(cubes)

print("The first three items in the list are: ")

i = 0

while i < 3:
    print(f"\t{cubes[i]}")
    i = i + 1
    
for num in cubes[:3]:
    print(num)

#4.11: My Pizzas, Your Pizzas.
my_pizzas = ["Hawaiian", "Seafood", "Greek"]
friends_pizzas = my_pizzas[:]

print("The types of pizza that I like are: ")
my_pizzas.append("Cheese")
for my_pizza in my_pizzas:
    print(f"\t{my_pizza}")
    
print("\nThe types of pizza that my friends like are: ")
friends_pizzas.append("peperoni")
for friends_pizza in friends_pizzas:
    print(f"\t{friends_pizza}")
    
#4.12: More Loops.
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

print("My favorite foods are: ")
for my_food in my_foods:
    print(f"\t{my_food}")
    
print("\nMy friend's favorite foods are: ")
for friend_food in friend_foods:
    print(f"\t{friend_food}")

#4.13: Buffet.
foods = ("Butter bread", "Dimsum", "Pho", "Tonkotsu", "Kimbap")

print("The five foods that the restaurant serves are: ")
for food in foods:
    print(f"\t{food}")

#foods.append("Noodle")

foods = ("Miso", "Dimsum", "Teriyaki Chicken and Rice", "Tonkotsu", "Kimbap")
print("\nThe new list of foods that the restaurant serves are: ")
for food in foods:
    print(f"\t{food}")

#4.14: PEP 8.
#Finished!

#4.15: Code Review.
#Do it yourself!
