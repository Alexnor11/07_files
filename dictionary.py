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


