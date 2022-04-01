from decimal import Decimal
from decimal import getcontext

print("Hello, I see you would like to calculate a raw food diet for your fur baby today.")
dog_weight = int(input("What is your dogs weight in lbs?"))


getcontext().prec = 3
food_total = round(float(Decimal(dog_weight * .03)), 2)

print(str(food_total) + ' grams')

food_comp = []
muscle = round((food_total * .7), 2)
edible_bone = round((food_total * .1), 2)
liver = round((food_total * .05), 2)
other_organs = round((food_total * .05), 2)
veggies = round((food_total * .07), 2)
seeds_nuts = round((food_total * .01), 2)
fruits = round((food_total * .01), 2)
food_comp.append(str(muscle) + ' grams' + ' of Muscle.')
food_comp.append(str(edible_bone) + ' grams' + ' of edible bone.')
food_comp.append(str(liver) + ' grams' + ' of liver.')
food_comp.append(str(other_organs) + ' grams'+ ' of other organs.')
food_comp.append(str(veggies) + ' grams' + ' of vegetables.')
food_comp.append(str(seeds_nuts) + ' grams' + ' seeds and nuts.')
food_comp.append(str(fruits) + ' grams' + ' fruits')


for item in food_comp:
    print ("Your dog needs " + item)


