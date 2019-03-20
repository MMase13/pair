name = input("what is your name? ")
age = input("How old you is? ")
color = input("Of all the colors in the pallet, which one appeases you the most? ")

print("I can't believe your mom named you " + name + ", you're " + age + " years old, but your favorite color is still " + color)

with open('weirdbeards.txt', 'a') as pairwork:
    pairwork.write("I can't believe your mom named you " + name + ", you're " + age + " years old, but your favorite color is still " + color)
