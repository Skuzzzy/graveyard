
def selection(arr):
    for n in xrange(len(arr)):
        minimum = arr[n]
        minindex = n
        for index in xrange(n, len(arr)):
            if arr[index] < minimum:
                minindex = index
                minimum = arr[minindex]
        arr[n], arr[minindex] = arr[minindex], arr[n]
    return arr

def insertion(arr):
    for index in xrange(1, len(arr)):
        search = index
        while search > 0 and arr[search-1] > arr[search]:
            arr[search-1], arr[search] = arr[search], arr[search-1]
            search -= 1
    return arr

def bubble(arr):
    for bottom in xrange(1, len(arr)):
        swap = False
        for index in xrange(len(arr)-1, bottom+1, -1):
            if arr[index] < arr[index-1]:
                arr[index-1], arr[index] = arr[index], arr[index-1]
                swap = True
        if not swap:
            return arr
    return arr

# Merge
# Shell ??
# Heap
# Quick
