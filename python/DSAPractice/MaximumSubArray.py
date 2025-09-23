

def max_subarray(A, low: int, high: int):
    # base case which is when 
    if high == low:
        return(low, high, A[low]) # can return A[low] or A[high] since equal
    else:
        mid = (low + high) // 2 # integer division so that it gives the mid
        (left_low, left_high, left_sum) = max_subarray(A, low, mid)
        (right_low, right_high, right_sum) = max_subarray(A, mid+1, high)
        (cross_low, cross_high, cross_sum) = max_crossing(A, low, mid, high)
        # checks for the highest sum and returns that
        if left_sum >= right_sum and left_sum >= cross_sum:  
            return(left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum: 
            return(right_low, right_high, right_sum)
        else:
            return(cross_low, cross_high, cross_sum)


def max_crossing(A, low, mid, high):
    # check the left subarray (from mid going left)
    left_sum = float('-inf')
    sum = 0
    max_left = mid  # initialize to avoid UnboundLocalError
    for i in range(mid, low-1, -1):  # Fixed: mid down to low (inclusive)
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
            
    # check the right subarray (from mid+1 going right) 
    right_sum = float('-inf')
    sum = 0
    max_right = mid + 1  # initialize to avoid UnboundLocalError
    for j in range(mid+1, high+1):  # Fixed: mid+1 to high (inclusive)
        sum += A[j]  # Fixed: was A[i], should be A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j  # Fixed: was i, should be j

    return(max_left, max_right, left_sum + right_sum)


def main() -> None:
    array = [-1, 2, 3, -4, 5, 6]
    low, high = 0, len(array) - 1  # Fixed: should be len(array) - 1
    left_max, right_max, max_array = max_subarray(array, low, high)

    print(f"Maximum subarray indices: {left_max} to {right_max}")
    print(f"Maximum sum: {max_array}")
    print(f"Subarray: {array[left_max:right_max+1]}")

if __name__ == "__main__":
    main()