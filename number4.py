with open("cars.txt", 'r', encoding="utf-8") as file:
    a = file.readlines()
count= {}
for i in range(1, len(a)):
    p = a[i].split('$')
    k = p[5]
    if k in count:
        count[k] += 1
    else:
        count[k] = 1
for line in count:
    print(str(count[line])+' машин цвета ' + line + ' есть сегодня в наличии ')