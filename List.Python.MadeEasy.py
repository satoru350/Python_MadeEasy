#List basic
friend_age = [17, 18, 19, 20, 21]
Monsters = ["Dragon", "Bahemoth", "Demon", "Spider"]
demon_index = Monsters.index("Demon")
print(demon_index)
print(Monsters[1])
print(Monsters[1:3])
Monsters[1] = "Succubus"
print(Monsters)
#
#List Basic Easy
Monsters = ["Dragon", "Bahemoth", "Demon", "Spider"]
Monsters[0] = "Loli Dragon"
Monsters[1] = "Chick"
Monsters[2] = "Demon Waifu"
Monsters[3] = "Spider Waifu"
print(Monsters)
#
#
#List add remove and lenth counting
ingredients = ["carrots", "potatoes", "onions"]

# Adding an ingredient
new_ingredient = input("Chef, a new ingredient has arrived! What is it? ")
ingredients.append(new_ingredient)
print("Perfect! The", new_ingredient, "has been added to the recipe.")

# Removing an ingredient
removed_ingredient = input("Uh-oh, Chef! We have an ingredient that needs to be removed. Which one is it? ")
if removed_ingredient in ingredients:
    ingredients.remove(removed_ingredient)
    print("Got it, Chef! The", removed_ingredient, "has been removed from the recipe.")
else:
    print("Apologies, Chef. The", removed_ingredient, "is not in the recipe.")

# Counting the number of ingredients
num_ingredients = len(ingredients)
print("Chef, we currently have", num_ingredients, "ingredients in our recipe.")

# Displaying the updated recipe
print("Here is our updated recipe:", ingredients)
#
#
#Checking membership of items in list
Monsters = ["Dragon", "Bahemoth", "Demon", "Spider"]
Monsters.remove("Demon")
if "Demon" in Monsters:
    print("Prepare the Demon Hunters!")
else:
    print("Let the Demon Hunters rest")
#
#
#
Monsters = ["Dragon", "Bahemoth", "Demon", "Spider"]
Monsters.remove("Demon")
Monsters.append("Demon Lord")
if "Demon" in Monsters:
    print("Prepare the Demon Hunters!")
elif "Demon Lord" in Monsters:
    print("Oh No! We're doomed!")
else:
    print("Let the Demon Hunters rest")
#
#
Monsters = ["Dragon", "Bahemoth", "Demon", "Spider"]

# List inserting an item at a specific index
Monsters.insert(1, "Giant")
print(Monsters)

# List length (Total number count)
count = len(Monsters)
print("There are", count, "monsters in the list.")

# Getting the strongest and weakest monsters
strongest = max(Monsters)
weakest = min(Monsters)
print("The strongest monster is", strongest)
print("The weakest monster is", weakest)
#
#
#Getting the lowest numbers and highest numbers in a list
numbers = [23, 43, 99, 1, 13, -21, 45]
print(min(numbers))
print(max(numbers))
#
#
# Check if a monster exists in the list
print("Bahemoth" in Monsters)
print("Vampire" in Monsters)
print("Demon" in Monsters)

# Combining two lists
friends = ["Batman", "Cat man", "Fat man"]
heroes = ["Superman", "Spider-Man", "Iron Man"]
all_characters = friends + heroes
print(all_characters)

# Removing the last monster
Monsters.pop()
print(Monsters)

# Extending one list with another
numbers = [1, 2, 3]
more_numbers = [4, 5, 6]
numbers.extend(more_numbers)
print(numbers)

# Counting the occurrence of a specific monster
count_of_dragon = Monsters.count("Dragon")
print("The number of Dragons in the list is", count_of_dragon)

# Sorting the monsters in alphabetical order
Monsters.sort()
print("Monsters sorted in alphabetical order:", Monsters)

# Creating a sorted copy of the monsters list
sorted_monsters = sorted(Monsters)
print("Sorted copy of the Monsters list:", sorted_monsters)
#
#
xeno = [2, 1, 6, 4, 8, 9, 0, 5, 6]
xeno.sort()
print(xeno)
#
xeno = [2, 1, 6, 4, 8, 9, 0, 5, 6]
sorted_xeno = sorted(xeno)
print(sorted_xeno)
#
#By the way list() function is used to convert something in list
#range(start, stop, step).
#The start parameter specifies the starting value of the range (inclusive),
#the stop parameter defines the ending value of the range (exclusive),
#and the step parameter sets the increment between values (default is 1).
#If only one parameter is given it'll be used as stop while start wil be 0
nums = list(range(5, 20, 2))
print(nums)
#
#
#range can be used in for loop. but output wouldn't be in list
for i in range(1, 6):
    print(i)
#
#














