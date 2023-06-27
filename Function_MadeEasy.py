#function basic 
def empire_war():
    print("prepare the army")
    print("take the sword")
    print("invade other nations")
    print("conquer other nations")
    print("expand the empire")
empire_war()
#
#
#  parameter(the variable inside parentheses)
def five_times(nums):# here nums is a parameter
    print(nums*5)
five_times(5)
five_times(20)
five_times(13)
#
#
# multiple parameters
def add_numbers(first, second):
    sum = first + second
    print(sum)

add_numbers(15, 10)
#
#
# parameters in functions act as placeholders for values that you provide when calling
# the function. They allow you to make your functions flexible and reusable, just
# like adding different ingredients to a recipe.
#
# Positional parameters*
def make_pizza(crust, toppings):
    # Code to make a pizza using the provided crust and toppings
    print("Making a", crust, "pizza with", toppings)

make_pizza("thin crust", "cheese, mushrooms")
#
# Keyword parameters*
def make_smoothie(fruit, yogurt, milk):
    # Code to make a smoothie using the provided ingredients
    print("Making a", fruit, "smoothie with", yogurt, "yogurt and", milk, "milk")

make_smoothie(fruit="banana", yogurt="vanilla", milk="almond")
#
# Default  parameters*
def make_smoothie(fruit, yogurt="vanilla", milk="almond"):
    # Code to make a smoothie using the provided ingredients
    print("Making a", fruit, "smoothie with", yogurt, "yogurt and", milk, "milk")

make_smoothie("strawberry")
#
# you can still override the default values by explicitly providing different values:
def make_smoothie(fruit, yogurt="vanilla", milk="almond"):
    # Code to make a smoothie using the provided ingredients
    print("Making a", fruit, "smoothie with", yogurt, "yogurt and", milk, "milk")

make_smoothie("blueberry", yogurt="Greek", milk="coconut")
#
#
#
# In retaurant you gave money and they give food,something in 'return',right?
# return statement is same,it gives u result,usually used in a function.
# The return statement allows you to retrieve the result or output of a
# function and use it elsewhere in your code.
# It works like print and ya forget about print inside sunction.
# Use return to send result from a function
#example
def add(a, b):
    return a + b

sum = add(13, 65)
print(sum)
#
# Another example
def square(number):
    result = number ** 2
    return result

x = 5
squared = square(x)
print("The square of", x, "is", squared)
#
# Daily life needs
def get_expense(tuition, rent):
    total = tuition + rent
    return total

expense = get_expense(5000, 3000)
print(expense)
#
# Odd number identify
def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True
    
is_odd = is_odd(17)
print(is_odd)
#
#
# an operation using return
def add(a, b):
    return a + b

x = add(2, 4)
y = add(4, 5)
z = add(x, y)
print(z)
#
# Another operation using return
def double_and_add(num1, num2):
    # Double each number
    doubled_num1 = num1 * 2
    doubled_num2 = num2 * 2

    # Add the doubled numbers
    sum_result = doubled_num1 + doubled_num2

    # Return the sum
    return sum_result

result = double_and_add(3, 4)
print("The sum of the doubled numbers is:", result)
#
#
# Some fun examples.
# Imagine you are a wizard that can turn things into gold using function! (Lol)
# Then the function would be :
def object_to_gold(object_name):
    transformed_object = "Gold " + object_name
    return transformed_object

result = object_to_gold("Ring")
print(result)
#
# Lets make a ditective themed function this time! 
# Here in the list inside the parameter(yea you can actually add them there),
# if fingerprints present then then the output would be affirmative
# Otherwise it will be a no.
def investigate_case(clues):
    if "fingerprints" in clues:
        return "The culprit left fingerprints!"
    return "No conclusive evidence found."

case_result = investigate_case(["footprints", "witness testimony", "fingerprints"])
print(case_result)
#
#
# How about a funcyion inside a function! Here's an culinary themed example :
def bake_cake():
    # Prepare the ingredients for the cake
    print("Preparing the cake batter...")

    # Mix the ingredients and bake the cake
    print("Mixing the ingredients...")
    print("Baking the cake...")

    # Return the freshly baked cake
    return "A delicious cake"

def decorate_cake():
    # Call the bake_cake function to get a freshly baked cake
    cake = bake_cake()

    # Start the decoration process
    print("Decorating the cake with frosting...")
    print("Adding colorful sprinkles...")
    print("Placing a cute cake topper...")

    # Return the beautifully decorated cake
    return "A beautifully decorated cake"

    # Let's create a masterpiece!
masterpiece = decorate_cake()

    # Enjoy the result of your culinary creation
print("Behold! You have created:", masterpiece)
#
#
#
#
#
# Lets do a fun yet kinda complex operation 
# Let's a function to create a magical potion this time!
# This function got conditions and loops. 
def create_potion(ingredients):
    potions = []  # Empty list to store potions
    
    for ingredient in ingredients:
        potion = "Unknown Potion"  # Default potion name
        
        if ingredient == "dragon scale":
            potion = "Dragonfire Elixir"
        elif ingredient == "unicorn horn":
            potion = "Elixir of Eternal Youth"
        elif ingredient == "phoenix feather":
            potion = "Phoenix Rebirth Tonic"
        elif ingredient == "mandrake root":
            potion = "Restorative Elixir"
        elif ingredient == "mermaid tears":
            potion = "Ocean's Serenity Brew"
        elif ingredient == "fairy dust":
            potion = "Enchanted Dreams Elixir"
        elif ingredient == "goblin earwax":
            potion = "Trollbane Elixir"
        else:
            print("Unknown ingredient:", ingredient)
        
        # Simulate the mixing process
        print("Stirring the cauldron...")
        print("Adding magical enchantments...")
        
        # Simulate additional processes (loops and conditions)
        for _ in range(3):
            print("Swirling the potion...")
        
        counter = 0
        while counter < 5:
            print("Magical sparks are dancing!")
            counter += 1
        
        potions.append(potion)  # Add the potion to the list
    
    # Return the list of created potions
    return potions

    # Let's gather some ingredients and create magical potions!
ingredients = ["dragon scale", "unicorn horn", "phoenix feather"]
magical_potions = create_potion(ingredients)

    # Display the magical potions created
for i, potion in enumerate(magical_potions):
    print("Potion", i+1, ":", potion)
#
#
#
#
# Another complex operation with two functions.
# this time you will be a intergalactic explorer and use the function to explore 
# resources from planets. Good luck!
def intergalactic_explorer(planet_names):
    # Prepare the spaceship for the intergalactic exploration
    resources_collected = []

    # Visit each planet in the list
    for planet in planet_names:
        # Conduct research and collect resources
        resources = explore_planet(planet)
        resources_collected.extend(resources)

    # Celebrate the successful mission and return the resources
    return resources_collected


def explore_planet(planet):
    # Simulate the exploration process
    print("Exploring planet", planet)
    resources = ["Crystals", "Ore", "Rare minerals"]
    print("Resources collected:", resources)

    # Return the resources gathered from the planet
    return resources

planets = ["Mercury", "Venus", "Mars", "Jupiter"]
collected_resources = intergalactic_explorer(planets)
print("We've returned with a bounty of cosmic resources:", collected_resources)
#
#
#