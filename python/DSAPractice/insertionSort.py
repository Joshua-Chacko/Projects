import random


def insertionSort(sortedArray):
    # start at 1st index
    # compare with index 1 to i-1
    # then sort 
    
    
    for i in range(1,len(sortedArray)):
        if i == 0:
            continue
        j = i
        while j > 0 and sortedArray[j] < sortedArray[j-1]:
            sortedArray[j], sortedArray[j-1] = sortedArray[j-1], sortedArray[j]
            j -= 1
    return sortedArray


def main():
    Array = [random.randint(0,10) for i in range(10)] 
    print(Array)
    print(insertionSort(Array))


if __name__ == "__main__":
    main()
