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


def food_print(*food_comp):
    for item in food_comp:
        print('Your Canine friend needs, ' + item)

food_print(*food_comp)


print("Now that we know how much of each of these things your dog needs, lets find out what exactly they all are.")
muscle_types = ["Chicken", 'Beef', 'Pork']
fruit_types = ['Blueberries','Apples','Bananas','Strawberries','Rasberries','Blackberries','Cranberries','Apricots','Oranges','Peaches','Pears','Mangoes','Pineapples','Coconut']
bone_types = ['Chicken wings', 'Chicken necks', 'Chicken legs', 'Chicken thighs', 'Turkey necks', 'Turkey', 'Lamb necks', 'Lamb ribs', 'Beef tail bones' ]
organ_types = ['Kidneys', 'Lungs', 'Hearts', 'Brains']
vegetable_types = ['Carrot', 'Sweet Potato', 'Peas', 'Broccoli', 'Celery', 'Green Beans', 'Cucumber', 'Cauliflower']
seed_types = ['Flax','Chia','Pumpkin','Sunflower']

class my_dictionary(dict):
    def __init__(self):
        self = dict()

    def add(self, key, *value):
        self[key] = value

food_type = my_dictionary()

food_type.add('Muscle Types', muscle_types )
food_type.add('Fruit Types', fruit_types)
food_type.add('Bone Types', bone_types)
food_type.add('Organ Types', organ_types)
food_type.add('Vegetable_types', vegetable_types)
food_type.add('Seed_types', seed_types)


print(food_type)


foods_to_avoid = ['Onions' , 'Garlic', 'Leeks', 'Scallions', 'Kale', 'Wild Picked Mushrooms', 'Raw Potatoes']

