
def LCS2(string1: str, string2: str):
    LCSlength = 0
    subString = ""

    rows = len(string1) + 1
    cols = len(string2) + 1

    matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(1,rows):
        for j in range(1,cols):
            if string1[i - 1] == string2[j - 1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    
    LCSlength = matrix[rows-1][cols-1]
    
    while matrix[rows-1][cols-1] != 0:
        if matrix[rows-1][cols-1] == matrix[rows-1][cols-2]: # to the left
            curr = string1[rows - 2]
            cols -= 1
        elif matrix[rows-1][cols-1] == matrix[rows-2][cols-1]: # above
            curr = string2[cols - 2]
            rows -= 1
        else:
            subString = string1[rows - 2] + subString
            rows -= 1
            cols -= 1

    for i in matrix:
        print(i)

    return LCSlength, subString

def main():
    test_cases = [
        ("abcde", "ace"),
        ("AGGTAB", "GXTXAYB"),
        ("abcdgh", "aedfhr"),
        ("abc", "abc"),
        ("abc", "def"),
        ("abcdefg", "xyzabc"),
        ("AXYT", "AYZX"),
        ("ABAZDC", "BACBAD"),
        ("aaaa", "aa"),
        ("XMJYAUZ", "MZJAWXU")
    ]

    for s1, s2 in test_cases:
        length, sub = LCS2(s1, s2)
        print(f'{s1} & {s2} → Length = {length}, LCS = "{sub}"')
        print('-' * 40)

if __name__ == '__main__':
    main()