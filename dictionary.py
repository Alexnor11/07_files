# Получить словарь из файла
with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    ingredient = {}

    for lis in file:
        lst = []
        name_dish = lis.strip()
        # Читаем кол-во итераций
        num = int(file.readline())
        for i in range(num):
            num = file.readline().strip().split('|')
            ingredient['ingredient_name'] = num[0]
            ingredient['quantity'] = num[1]
            ingredient['measure'] = num[2]
            lst.append(ingredient.copy())

        cook_book[name_dish] = lst
        file.readline()

print(cook_book)
print()


# Задача №2 Список блюд и кол-во персон
def get_shop_list_by_dishes(dishes, person_count):
    order = {}
    for dish in dishes:
        list_ingredient = cook_book[dish]
        for r in list_ingredient:
            ing_name = r['ingredient_name']
            order[ing_name] = {'measure': r['measure'], 'quantity': int(r['quantity']) * person_count}

    print(order)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
get_shop_list_by_dishes(['Утка по-пекински'], 3)
