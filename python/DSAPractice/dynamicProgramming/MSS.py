def MSS(array: list):
    mss = float('-inf')
    # mssarray <-- [0.. len(array)-1]
    mssArray = [0] * len(array)
    # for i <-- 0 to len(array) - 1
    for i in range(len(array)):
        # mssarray[i] = max(array[i], array[i] + mssarray[i-1])
        mssArray[i] = max(array[i], array[i] + mssArray[i-1])
        # if mssarray[i] > mssarray[i-1]:
        if mssArray[i] > mss:
            # mss = mssaray[i]
            mss = mssArray[i]
    return mss



def main():
    array = [5, -1, 2, -3, 7, -2, 3]
    print(MSS(array))


if __name__ == '__main__':
    main()