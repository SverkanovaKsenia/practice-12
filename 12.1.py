import json

with open("products.json", "r", encoding='utf-8') as read_file:
    data = json.load(read_file)

for product in data["products"]:
    print("Название: " + product["name"])
    print("Цена: " + str(product["price"]))
    print("Вес: " + str(product["weight"]))
    if product["available"]:
        print("В наличии")
    else:
        print("Нет в наличии!")
    print()