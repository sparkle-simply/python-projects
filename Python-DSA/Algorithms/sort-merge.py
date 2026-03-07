# The Merge Sort algorithm is a divide-and-conquer algorithm that sorts an array by first breaking it down into smaller arrays,
# and then building the array back together the correct way so that it is sorted.

def mergeSort(arr, start, end):
  if end - start <= 1:
    return arr[start:end]

  mid = (start + end) // 2
  sortedLeft = mergeSort(arr, start, mid)
  sortedRight = mergeSort(arr, mid+1, end)
  return merge(sortedLeft, sortedRight)

def merge(left, right):
  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  return result

mylist = [3, 7, 6, -10, 15, 23.5, 55, -13]
mysortedlist = mergeSort(mylist)
print("Sorted array:", mysortedlist)