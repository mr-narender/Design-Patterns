# This is a sample Python script.
# Examples of set uses

fruit = {'apples', 'pears', 'lemons'}
fruitPie = {'apples', 'pears'}

# both are true if fruitPie
# is a member of fruit
print (fruitPie.issubset(fruit))
print (fruitPie < fruit)

# combine sets
nuts = {'walnuts', 'pecans'}
granola = fruit | nuts
print(granola)

data = {2.3, 4.6, 7.0}
print (data)