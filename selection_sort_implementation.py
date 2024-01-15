#selection sort implementation

def selection_sort(arr):

    for i in range(len(arr)):

      min=arr[i]

      for j in range(i+1,len(arr)):

          if arr[j]<arr[i]:
            arr[i],arr[j]=arr[j],arr[i]

    return arr

#driver code
arr=[1,5,3,2,4,8,6,7]
print(selection_sort(arr))
