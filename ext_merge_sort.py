"""
Use any kind of External Sorting algorithm to
sort all numbers from input/unsorted_*.txt files
and save the sorted result into output/sorted.txt
file amd async_sorted.txt file.
"""

#K-way merge of stuff in the files
import glob
import heapq

def merge(left, right, arr):
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def sort(arr): #merge sort
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        sort(left)
        sort(right)
        merge(left, right, arr)

#kway merge
def create_fileHandles(fileHandlers, q):
    path = "output/sorted_*.txt"
    for filename in glob.glob(path): #open all sorted subsections and store open file handles in a list
        f = open(filename, "r")
        fileHandlers.append(f)

#file_handlers = []
def sort_sets():
    path = "input/unsorted_*.txt"
    count = 1
    for filename in glob.glob(path):
        temp = []
        with open(filename, 'r') as f:
            for line in f:
                temp.append(int(line))
        f.close()
        sort(temp)
        with open("output/sorted_" + str(count) + ".txt", 'w') as f:
            f.writelines(str(line) + "\n" for line in temp)
        f.close()
        count += 1

def kway_merge(fileHandlers, q):
    with open("output/sorted.txt", "w") as f:
        count = len(fileHandlers)
        while count > 0:
            for idx, fh in enumerate(fileHandlers): #perform k-way merge with priority heap
                try:
                    temp = int(fh.readline()) #get next value and cast to int
                except ValueError:
                    fh.close()
                    del fileHandlers[idx]
                    count -= 1
                    continue
                try:
                    heapq.heappush(q, temp)
                except MemoryError:
                    while q:
                        top = heapq.heappop(q)
                        f.write(str(top) + "\n")
                        #write everything in heap to file and clear the heap
        while q:
            top = heapq.heappop(q)
            f.write(str(top) + "\n")
    f.close()

def main():
    sort_sets()
    fileHandlers = []
    q = []
    create_fileHandles(fileHandlers, q)
    #kway merge
    kway_merge(fileHandlers, q)


if __name__ == "__main__":
    main()







