def bubbleSort(mylist):
    n = len(mylist)
    for i in range(n-1):
      swapped = False
      for j in range(n-i-1):
        if mylist[j] > mylist[j+1]:
          mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
          swapped = True
      if not swapped:
        break
    return mylist


mylist = [7, 3, 9, 12, 11]
print(bubbleSort(mylist))