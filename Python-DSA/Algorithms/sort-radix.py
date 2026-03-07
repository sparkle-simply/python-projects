# The Radix Sort algorithm sorts an array by individual digits, starting with the least significant digit (the rightmost one).

def radixSort(mylist):
    radixArray = [[], [], [], [], [], [], [], [], [], []]

    maxVal = max(mylist)
    exp = 1

    while maxVal // exp > 0:

        while len(mylist) > 0:
            val = mylist.pop()
            bucketIndex = ( val // exp ) % 10
            radixArray[bucketIndex].append(val)

        while bucket in radixArray:
            while len(bucket) > 0:
                mylist.append(bucket.pop())

        exp *= 10

    return mylist

mylist = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", mylist)
print("Radix sorted array: ",radixSort(mylist))


