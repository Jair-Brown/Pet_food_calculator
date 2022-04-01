from decimal import Decimal
from decimal import getcontext


dog_weight = int(input("Dogs_weight in lbs?"))


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
food_comp.append("Muscle " + str(muscle) + ' grams')
food_comp.append('Edible Bone ' + str(edible_bone) + ' grams')
food_comp.append('Liver ' + str(liver) + ' grams')
food_comp.append('Other Organs ' + str(other_organs) + ' grams')
food_comp.append('Vegetables ' + str(veggies) + ' grams')
food_comp.append('Seeds and Nuts ' + str(seeds_nuts) + ' grams')
food_comp.append('Fruits ' + str(fruits) + ' grams')

#print(food_comp)
for item in food_comp:
    print (item)


#print('Hello, your canine companion needs '+ )
