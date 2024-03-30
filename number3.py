with open("cars.txt", 'r', encoding="utf-8") as file:
    a = file.readlines()
max_input,min_input = map(str,input().split())
while max_input != 'стоп':
    max_input=int(max_input)
    min_input=int(min_input)
    numb = 0
    for i in range(1, len(a)):
        p = a[i].split('$')
        if int(p[0])>=min_input and int(p[0])<=max_input:
            numb+=1
            manufacturer = p[2]
            model = p[3]
            price=p[0]
            odometer=p[4]
            if numb==1:
                print('Исходя из вашего бюджета:', min_input, '-', max_input, 'найдены следующие варианты:','\n', '\t', numb, '.',manufacturer, model, 'цена', str(price)+', пробег данной машины составляет', odometer,'\n')
            elif numb>1:
                print('\t', numb,'.',manufacturer, model,'цена', str(price)+', пробег данной машины составляет', odometer, '\n')
    if numb == 0: print('К сожалению, под ваш бюджет ничего не удалось найти')
    max_input, min_input = map(str,input().split())