'''def first():
    """Описание функции first.

        Функция анализирует данный файл и создает новый согласно заданному условию.

        """
    alist = []
    langs = []'''
alist = []
langs = []
with open('cars.txt', 'r', encoding="utf-8") as file:
    header = "manufacturer;model;paint_color;odometer;price"
    line = file.readline()
    for line in file:
        line = line.split("$")
        if float(line[4])<10000:
            line[5].replace('\n', ' ')
            alist.append([line[2], line[3], str(line[5])+str(line[4]), line[0]])
        if float(line[4])<10000 and line[5]=='серебро':
            langs.append([line[2], line[3], 'есть машина серебряного цвета. Ее стоимость', line[0], 'и пробег:',line[4]])

with open("odometer_car.txt ", 'w', encoding="utf-8") as out_file:
    out_file.write(header + "\n")
    for line in alist:
        line = " ".join(line)
        out_file.write(line)
print(langs)

