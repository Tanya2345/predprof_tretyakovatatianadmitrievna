
def quicksort(alist,start,end):
    i=start
    j=end
    pivot=alist[(start+end)//2]

    while True:
        while alist[i]<pivot:
            i+=1
        while alist[j]>pivot:
            j-=1
        if i<=j:
            alist[i], alist[j]=alist[j],alist[i]
            i+=1
            j-=1
        else:
            break
    if start<j:
        quicksort(alist,start,j)
    if i<end:
        quicksort(alist,i,end)
    return alist

def second():
    alist = []
    with open("cars.txt", 'r', encoding="utf-8") as file:
        line1 = file.readline()
        for line1 in file:
            line = line1.split("$")
            alist.append(line)
    alist = quicksort(alist,str(line1[0][0]),str(line1[-1][0]))
    for i in range(3):
        print(f" Вам могут подойти: {alist[i][2]},{alist[i][3]}, ;Цвет {alist[i][5]}, ;Пробег{alist[i][4]}, ;Цена:{alist[i][0]}")
    print(header)
second()
