#5.1: Conditional Tests.
car = "Subaru"

print("Is car == 'Subaru'? I predict True!")
print(car == "Subaru")

print("\nIs car == 'Audi'? I predict False!")
print(car == "Audi")

#5.2: More Conditional Tests.
#Skip!

#5.3: Alien Colors #1.
#Pass test.
alien_color = "green"

if alien_color == "green":
    print("You just earned 5 pts")

#Fail test.
alien_color = "green"

if alien_color == "red":
    print("You just earned 5 pts")

#5.4: Alien Colors #2.
#If block.
alien_color = "green"

if alien_color == "green":
    print("You just earned 5 pts!")
else:
    print("You just earned 10 pts!")

#Else block.
alien_color = "red"

if alien_color == "green":
    print("You just earned 5 pts!")
else:
    print("You just earned 10 pts!")

#5.5: Alien Colors #3.
#Green.
alien_color = "green"

if alien_color == "green":
    print("You just earned 5 pts!")
elif alien_color == "yellow":
    print("You just earned 10 pts!")
else:
    print("You just earned 15 pts!")

#Yellow
alien_color = "yellow"

if alien_color == "green":
    print("You just earned 5 pts!")
elif alien_color == "yellow":
    print("You just earned 10 pts!")
else:
    print("You just earned 15 pts!")

#Red
alien_color = "red"

if alien_color == "green":
    print("You just earned 5 pts!")
elif alien_color == "yellow":
    print("You just earned 10 pts!")
else:
    print("You just earned 15 pts!")

#5.6: Stages of Life.
age = int(input("Please enter your age: "))

if age < 2:
    print("You are a baby.")
elif age > 2 and age < 4:
    print("You are a toddler.")
elif age > 4 and age < 13:
    print("You are a kid.")
elif age > 13 and age < 20:
    print("You are a teenager.")
elif age > 20 and age < 65:
    print("You are an adult.")
else:
    print("You are an elder.")

#5.7: Favorite Fruit.
fav_foods = ["Ramen", 
            "Cheesecake", 
            "Teriyaki Chicken"] #PEP 8 style?

if "Ramen" in fav_foods:
    print("I really enjoy Ramen!")
if "Durian" in fav_foods:
    print("I really enjoy Durian!")
if "Cheesecake"in fav_foods:
    print("I really enjoy Cheesecake!")
if "Fried Chicken" in fav_foods:
    print("I really enjoy Friend Chicken!")
if "Teriyaki Chicken" in fav_foods:
    print("I really enjoy Teriyaki Chicken!")

#5.8: Hello Admin.
user_name = ["admin", "jul", "wub_wub", "ola", "app00Jul"]
enter_user = input("Please enter your user name: ")
if enter_user == "admin" in user_name:
    print("Hello Admin, would you like to see a status report?")
elif enter_user in user_name:
    print(f"Wellcome {enter_user}, thank you for using our service again!")
else:
    print(f"Sorry but user name '{enter_user}' is not avaible in our system. Please try again!")

#5.9: No Users.
user_names = []

if user_names:
    for user_name in user_names:
        print(user_name)
else:
    print("We need more user!!!")

#5.10: Checking Usernames.
current_users = ["admin", "jul", "wub_wub", "ola", "app00Jul"]
new_users = ["hek", "jul", "dida", "cassie", "app00Jul"]

for new_user in new_users:
    if new_user in current_users:
        print(f"This user name '{new_user}' is already available. Please try a different one!!!")
    else:
        print(f"The user name '{new_user}' is valid. Thank you for using our service.")

#5.11: Ordinal Numbers.
numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
    
#5.12: Styling if statements.
#Skip!

#5.13: Your ideas.
#Skip!
