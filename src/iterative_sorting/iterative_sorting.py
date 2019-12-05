# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
  # loop through n-1 elements
  for i in range(0, len(arr) - 1):
    cur_index = i
    smallest_index = cur_index
    # TO-DO: find next smallest element
    # (hint, can do in 3 loc) 
    for j in range(i+1, len(arr)):
      if arr[j] < arr[smallest_index]:
        smallest_index = j

    # TO-DO: swap
    if smallest_index != cur_index:
      temp = arr[cur_index]
      arr[cur_index] = arr[smallest_index]        
      arr[smallest_index] = temp        


  return arr

print(selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
  swapped = True
  for i in range(len(arr)):
    # if swap wasnt set to True during last iteration
    # break out of the loop
    if swapped == False:
      break
    swapped = False

    for j in range(len(arr) - 1):
      # swap
      if arr[j+1] < arr[j]:
        temp = arr[j]
        arr[j] = arr[j+1]        
        arr[j+1] = temp                 
        swapped = True

  return arr

print(bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

  return arr