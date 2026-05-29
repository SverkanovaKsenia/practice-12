import json

with open("products.json", "r", encoding='utf-8') as read_file:
    products_data = json.load(read_file)

print("Введите данные о новом продукте:")
name = input("Название: ")
price = int(input("Цена: "))
weight = int(input("Вес: "))
available = input("В наличии? (да/нет): ")
if available == "да":
    available = True
else:
    available = False

new_product = {
    "name": name,
    "price": price,
    "available": available,
    "weight": weight
}
products_data["products"].append(new_product)

with open("products.json", "w", encoding='utf-8') as write_file:
    json.dump(products_data, write_file, ensure_ascii=False, indent=2)

print("")
print("Текущий список продуктов:")
print("")

for product in products_data["products"]:
    print("Название: " + product["name"])
    print("Цена: " + str(product["price"]))
    print("Вес: " + str(product["weight"]))
    if product["available"]:
        print("В наличии")
    else:
        print("Нет в наличии!")
    print("")