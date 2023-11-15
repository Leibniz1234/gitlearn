import time


def SelectionSort(array):
    
    # for i in range(len(array)):
    #     min_index = i
    #     for j in range(i, len(array)):
    #         if array[j] <= array[min_index]:
    #             min_index = j
    #     array[i], array[min_index] = array[min_index], array[i]
    # print("SelectionSort", array)            

    for i in range(len(array)-1, 0, -1):
            max_index = i

            for j in range(0, i):
                if array[j] >= array[max_index]:
                    max_index = j
            array[i], array[max_index] = array[max_index], array[i]
    print(array)    


def BubbleSort(array):
    for i in range(1, len(array)):
        for j in range(0, len(array)-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    print("buble sort", array)


def InsertionSort(array):
    for i in range(0,len(array)-1):
        new_card = array[i]
        j = i-1
        while(j>=0 and array[j]>new_card):
            array[j+1] = array[j]
            j -= 1
        array[j+1] = new_card
       

def MergeSort(array):
    n = len(array)
    if n<=1:
        return array
    mid = n//2
    left_array = array[:mid]
    right_array = array[mid:]
    MergeSort(left_array)
    MergeSort(right_array)

    left = len(left_array)
    right = len(right_array)
    i = 0
    j = 0
    k = 0
    while  i < left and j < right:
        if left_array[i] > right_array[j]:
            array[k] = right_array[j]
            j += 1
           
        else:        
            array[k] = left_array[i]
            i += 1
        k += 1
    while i < left:
        array[k] = left_array[i]
        i += 1
        k += 1 
    while j < right:
        array[k] = right_array[j]
        j += 1
        k += 1         



def QuickSort(array, l, r):
    if r <= l:
        return 
    p = Partition(array,l, r)
    QuickSort(array, l, p-1)
    QuickSort(array, p+1, r)


def Partition(array, l, r):
    pivot = array[r]
    i = l-1
    for j in range(l, r):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
            
    array[i+1], array[r] =  array[r], array[i+1]    
    return i+1  



array = [1,4,2,5,3,6,0,8,6,4,5,3,45,5,6,3,2,2,1,4,5,6]
# selection

# start1 = time.time()
# SelectionSort(array)
# print("Selection sort:",time.time()-start1)
  

# bubble  
# start2 = time.time()
# BubbleSort(array)
# print("Bubble sort:",time.time()-start2)


# insertion
# InsertionSort(array)
# print("Insertionsort", array) 


# merge sort
# MergeSort(array)
# print("mergesort", array)

QuickSort(array,0,len(array)-1)
print("Quicksort", array)