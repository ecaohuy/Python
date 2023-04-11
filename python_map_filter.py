menu = ["esprresso", "latte", "cappuccino", "mocha", "americano"]
def find_coffee(coffee):
    if coffee[0] == "c":
        return coffee
map_coffee = map(find_coffee, menu)
for x in map_coffee:
    print(x)
print("------")

filter_coffee = filter(find_coffee, menu)
for x in filter_coffee:
    print(x)