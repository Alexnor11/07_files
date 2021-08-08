files = ['1.txt', '2.txt', '3.txt']
my_dict = []
for i in files:
    with open(i, 'r', encoding='utf-8') as file:
        my_dict.append(f"Имя файла: {i} \n")
        my_dict.append(f"Количество строк: {len(file.readlines())} \n")
        file.seek(0)
        my_dict.append(f"{file.read()} \n\n")
        s = my_dict.copy()

print(s)

with open('03_task.txt', 'w', encoding='utf-8') as f:
    f.writelines(my_dict)
