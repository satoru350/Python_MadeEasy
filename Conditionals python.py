#An example on Conditionals
age = 17
huge_headphone = True

if age > 30 and huge_headphone == True:
    print("He's the hacker!")
elif age > 25 and huge_headphone == True:
    print("He's very suspicious.")
elif age > 25 and huge_headphone == True:
    print("He's somewhat suspicious.")
elif age > 20 and huge_headphone == True:
    print("He's not very suspicious.")
elif age > 20 or huge_headphone == False:
    print("Seems like an ordinary person.")
elif age > 15:
    print("Just a kid with headphones.")
else:
    print("Let him go.")

