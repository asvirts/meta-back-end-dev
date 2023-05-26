menu = ["Cold brew", "Espresso", "Mocha", "Latte", "Cappuccino", "Americano"]


def find_coffee(coffee):
    if coffee[0] == "C":
        return coffee


# Map
print("Map method:")
map_coffee = map(find_coffee, menu)

for i in map_coffee:
    print(i)
print()

# Filter
print("Filter method:")
filter_coffee = filter(find_coffee, menu)

for i in filter_coffee:
    print(i)
