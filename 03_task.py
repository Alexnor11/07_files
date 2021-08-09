import operator

files = ['1.txt', '2.txt', '3.txt']
f_dict = {}

for i in files:
    with open(i, 'r', encoding='utf-8') as file:
        text_read = file.readlines()
    count = len(text_read)
    f_dict[i] = count

f_sorted = sorted(f_dict.items(), key=operator.itemgetter(1))

with open('03_task.txt', 'w', encoding='utf-8') as f:
    for i in f_sorted:
        f.write(f"\n{i[0]} \n")
        f.write(str(i[1]) + '\n')

        with open(i[0], 'r', encoding='utf-8') as f_read:
            for line in f_read:
                # print(line)
                f.write(line)

