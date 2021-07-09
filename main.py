# this type of sort is fast compared with the merge sort and the inserting sort and has some useful applications
# like priority queue
# the time complexity of this algorithm is O(n lg n)
# highly recommended to see this (https://visualgo.net/en/heap?slide=1)
# ( 10 / 7 / 2021)
def MaxHeapify(array, i, lengthHeap):
    leftChild = int(2 * i) + 1
    rightChild = int((2 * i)) + 2
    largest = i

    if leftChild < lengthHeap and array[leftChild] > array[i]:  # comparing if the left child is smaller than the size
        largest = leftChild                         # of the heap
    if rightChild < lengthHeap and array[rightChild] > array[largest]:   # note that it's comparing with the largest
        largest = rightChild                                       # to see if the right child is greater
    if largest != i:
        array[i], array[largest] = array[largest], array[i]  # swapping
        MaxHeapify(array, largest, lengthHeap)


def HeapSort(array):
    lengthHeap = len(array)                                     # building the max heap from the array
    for i in range(len(array), -1, -1):
        MaxHeapify(array, i, lengthHeap)

    for i in range(lengthHeap - 1, 0, -1):                      # extracting the max element and then check if the max
        array[i], array[0] = array[0], array[i]                 # heap sorting condition isn't violated
        MaxHeapify(array, 0, i)                                 # the condition is array[parent(i)] >=  array[i]


testArray = [2, 5, 3, 8, 6, 5, 4, 7]
HeapSort(testArray)
print("the sorted array is ", testArray)
