# The lowest value is identified and is placed at first position
def selectionSort(mylist):
    n = len(mylist)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if mylist[j] < mylist[min_index]:
                min_index = j
        mylist[i], mylist[min_index] = mylist[min_index], mylist[i]
    return mylist

mylist = [64, 32, 9, 7, 12, 11, 76, 19]
print(selectionSort(mylist)
