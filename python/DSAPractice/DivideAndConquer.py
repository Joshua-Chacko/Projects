import random



def DC(Array):
    length = len(Array)
    if len(Array) <= 1:
        return

    mid = length // 2
    leftArray = [Array[i] for i in range(mid)] 
    rightArray = [Array[i] for i in range(mid, length)] 
    merged_array = []
    DC(leftArray)
    DC(rightArray)
    merge_sorted(leftArray, rightArray, Array)


def merge_sorted(left, right, Array):
    leftSize = len(left)
    rightSize = len(right)
    i = 0
    l = 0
    r = 0
    while l < leftSize and r < rightSize:
        if left[l] < right[r]:
            Array[i] = left[l]
            i += 1
            l += 1
        else:
            Array[i] = right[r]
            i += 1
            r += 1
    while l < leftSize:
        Array[i] = left[l]
        i += 1
        l += 1
    while r < rightSize:
        Array[i] = right[r]
        i += 1
        r += 1
    

def main():
    Array = [random.randint(0,10) for i in range(10)] 
    print(Array)
    DC(Array)
    print(Array)

    
if __name__ == "__main__":
    main()
