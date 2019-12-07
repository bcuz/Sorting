# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
  merged_arr = []
  i = 0
  j = 0

  # while we havent reached the end of both arrays
  while i < len(arrA) or j < len(arrB):

    # if we've placed all the elements in arrA,
    # put the rest of the elements in arrB into the merged_arr
    if i == len(arrA):
      merged_arr.append(arrB[j])
      j += 1
    # vice versa of above
    elif j == len(arrB):
      merged_arr.append(arrA[i])
      i += 1      
    # if the current in arrA is less than the current element,
    # if arrB, put the element from arrA into the merged arr
    elif arrA[i] < arrB[j]:
      merged_arr.append(arrA[i])
      i += 1    
    # vice versa of above
    elif arrA[i] > arrB[j]:
      merged_arr.append(arrB[j])
      j += 1
  
  return merged_arr

# print(merge([1,3,5], [2,4,6]))
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
  # TO-DO
  if (len(arr) <= 1):
    return arr
  
  middleIndex = len(arr) // 2

  # arr up to middle index (not inclusive)
  left = merge_sort(arr[:middleIndex])
  # arr from middle index (inclusive)
  right = merge_sort(arr[middleIndex:])

  return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
  # TO-DO

  return arr

def merge_sort_in_place(arr, l, r): 
  # TO-DO

  return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

  return arr
