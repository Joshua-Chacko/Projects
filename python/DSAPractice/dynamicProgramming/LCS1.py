def LCS1(string1 , string2):
    print(string1)
    print(string2)
    maxLCS = 0
    subString = ""
    maxIndex = (0,0)

    rows = len(string1) + 1
    columns = len(string2) + 1
    
    matrix = [[0 for _ in range(columns)] for _ in range(rows)]

    for row in range(1,rows):
        for col in range(1,columns):
            if string1[row-1] == string2[col-1]:
                matrix[row][col] = matrix[row-1][col-1] + 1
            if matrix[row][col] > maxLCS:
                maxLCS = matrix[row][col]
                maxIndex = (row,col)
    row, col = maxIndex
    while matrix[row][col] != 0:
        subString = string1[row-1] + subString  # prepend character
        row -= 1
        col -= 1
    for row in matrix:
        print(row)
    return maxLCS, subString


def main():
    string1, string2 = "aaabaaa", "abaa"
    length, subString = LCS1(string1, string2)
    print(f'Length = {length} and Substring = {subString}')

if __name__ == '__main__':
    main()