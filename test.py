from decimal import Decimal
from decimal import getcontext

print("Hello, I see you would like to calculate a raw food diet for your fur baby today.")
dog_weight = int(input("What is your dogs weight in lbs?"))


getcontext().prec = 3
food_total = float(Decimal(dog_weight * .03))

print(str(food_total) + ' grams')

food_comp = []
muscle = (food_total * .7)
edible_bone = (food_total * .1)
liver = (food_total * .05)
other_organs = (food_total * .05)
veggies = (food_total * .07)
seeds_nuts = (food_total * .01)
fruits = (food_total * .01)
food_comp.append(str(muscle) + ' grams' + ' of Muscle.')
food_comp.append(str(edible_bone) + ' grams' + ' of edible bone.')
food_comp.append(str(liver) + ' grams' + ' of liver.')
food_comp.append(str(other_organs) + ' grams'+ ' of other organs.')
food_comp.append(str(veggies) + ' grams' + ' of vegetables.')
food_comp.append(str(seeds_nuts) + ' grams' + ' seeds and nuts.')
food_comp.append(str(fruits) + ' grams' + ' fruits')


for item in food_comp:
    print ("Your dog needs " + item)


