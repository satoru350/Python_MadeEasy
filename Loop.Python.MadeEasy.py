# for loop 
#Imagine you are a conductor holding a baton and leading
#a bunch of musicians. You lead each musisians to play
#Their role. your baton here will be for loop
# List of musicians
musicians = ["Violinist", "Pianist", "Guitarist", "Drummer"]

# Conductor's instructions
for musician in musicians:
    print("It's time for the", musician, "to play their instrument!")

print("The performance has ended. Well done, musicians!")
#
#Other examples
#for loop
basket = ["Apple", "Orange", "Strawberry"]
for fruit in basket:
    massage = "Fresh" + " " + fruit
    print(massage)
#
#
#
basket = ["Apple", "Orange", "Strawberry"]
for fruit in basket:
    massage = "Fresh " + fruit
    print(massage)
#
#
#
# The treasure map: steps to the hidden treasure
treasure_map = list(range(1, 11))
for step in treasure_map:
    print("Step", step, "– Keep moving forward!")

print("Congratulations! You've reached the hidden treasure!")

# Conditon inside a loop
nums = [12, 54, -21, 213, 56, 35, 99, 24, 85, 72, 20]
for num in nums:
    if num > 0:
        print(num)
#
# Lets take it in a fun way#
#Imagine you are a ditective!
# List of clues
clues = ["witness saw a tall figure", "footprints match a specific shoe brand", "a note with a mysterious symbol"]

# Investigating the clues
for clue in clues:
    if "tall" in clue:
        print("The suspect might be tall!")
    elif "footprints" in clue:
        print("We should look for someone wearing that shoe brand!")
    elif "note" in clue:
        print("The mysterious symbol on the note could be a vital clue!")
    else:
        print("This clue doesn't seem relevant.")

print("Case solved! The mystery has been unraveled.")
#
#
# if the current clue is "witness saw a tall figure", the condition if "tall
# in clue: would evaluate to True because the word "tall" is indeed present
# within the string.
# To make the code more easy to understand, here's a modified code with the
# use of string formatting (f"...") to include the actual clue value in the
# printed messages.
# List of clues
clues = ["witness saw a tall figure", "footprints match a specific shoe brand", "a note with a mysterious symbol"]

# Investigating the clues
for clue in clues:
    if "tall" in clue:
        print(f"The clue '{clue}' suggests the suspect might be tall!")
    elif "footprints" in clue:
        print(f"The clue '{clue}' indicates we should look for someone with matching shoe brand!")
    elif "note" in clue:
        print(f"The clue '{clue}' unveils a mysterious symbol that could be important!")
    else:
        print(f"The clue '{clue}' doesn't seem relevant.")

print("Case solved! The mystery has been unraveled.")
#
# by the way here the f"..." is used. The f-string f"..." takes the value of
# a variable and replaces the placeholder {} with that value. The
# braces {}
#
#
#break loop
treasure_map = [4, 2, 6, 8, 3, 5, 1, 7]

for room_number in treasure_map:
    if room_number == 3:
        print("Found the treasure!")
        break
    else:
        print("Not here. Keep searching...")
#
#
#continue loop (skipping)
#Imagine room 2 got a monster,so you wanna skip it!
treasure_map = [4, 2, 6, 8, 3, 5, 1, 7]

for room_number in treasure_map:
    if room_number % 2 == 0:
        continue
    print(room_number)
#
# More examples
toys = ["ball", "puzzle", "teddy bear", "lego", "car"]
for toy in toys:
    if toy == "lego":
        print("Oh no, it's a lego! I'll deal with it later.")
        continue
    print("Cleaning", toy)

print("Room cleaning complete!")
#
#
# while loop
#
count = 0
while count < 10:
    print(count)
    count = count + 1
#
# while loop in a fun way
riding = True

while riding:
    print("Wheee! Riding Python Loop!")
    ask = input("Do you want to ride again? (yes/no): ")

    if ask.lower() == "no":
        riding = False

print("Thanks for riding Python Loop! Come back soon!")
#
#
# *Usage of while loop*
#
# Sum even numbers from 1 to 10
i = 1
sum = 0
while i <= 10:
    if i%2 == 0:
        sum = sum + i
    i = i + 1
print(sum)
#
#
# Sum odd numbers from 1 to 10
i = 1
sum = 0
while i <= 10:
    if i%2 != 0:
        sum = sum + i
    i = i + 1
print(sum)
#
#
# continue inside while loop
#(If count varible is placed after continue,if will ignore the count imcrement and
# the loop will be infinity zeros. also if variable is written before 'if' statement
# then the code will produce +1,ignoring the zero which goes for both continue and break)
i = 0
while i < 5:
    if i == 3:
        i += 1
        continue  
    print(i)
    i += 1

#
#
# break inside while loop
# (unlike the continue,if increment comes before break statement but after 'if' then 
# if will ignore the increment and produce infinity zeros)
# Example with break statement
i = 0
while i < 5:
    if i == 3:
        break  
    print(i)
    i += 1
#
# you can plaze print above break statement,result will be same.
i = 0
while i < 5:
    print(i)
    if i == 3:
        break  
    i += 1
# same goes for continue
i = 0
while i < 5:
    print(i)
    if i == 3:
        i += 1
        continue  
    i += 1
#
#
#more example
chest_coins = [10, 5, 8, 12, 3]
total_sum = 0
index = 0

while index <= len(chest_coins) - 1:
    coins = chest_coins[index]
    total_sum += coins
    index += 1

print("Congratulations! You've collected a total of", total_sum, "coins!")
#
#























