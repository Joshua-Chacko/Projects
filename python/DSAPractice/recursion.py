

def factorial(n):
    if n == 0 or n == 1: # base case n = 0 or n = 1 factorial is 1
        return 1 
    return n * factorial(n-1) # recursion to calculate factorial

def power(n, m):
    # base case if m = 1 return the value of n 
    # base case two if m = 0 return 1 
    if m == 1:
        return n
    elif m == 0:
        return 1        
    return n * power(n, m-1) 
    
def sumOfNaturalNumber(n):
    # base case n = 1 sum is 1
    if n == 1:
        return 1
    return n + sumOfNaturalNumber(n-1)

def countDigits(n):
    # base case 
    if n < 10:
        return 1
    return 1 + countDigits(n // 10)
    

def sumOfDigits(n):
    if n < 10:
        return n
    return (n%10) + sumOfDigits(n//10)

def reverseNumber(n):
    """
    Recursively reverse the digits of a positive integer.
    
    Args:
        n: A positive integer
    
    Returns:
        The number with its digits reversed
    """
    # Helper function that does the actual recursion
    def reverse_helper(num, reversed_num=0):
        # Base case: when no more digits left
        if num == 0:
            return reversed_num
        
        # Get the last digit
        last_digit = num % 10
        
        # Add this digit to our reversed number
        # Shift reversed_num left by multiplying by 10, then add the digit
        new_reversed = reversed_num * 10 + last_digit
        
        # Remove the last digit from original number and recurse
        return reverse_helper(num // 10, new_reversed)
    
    return reverse_helper(n)

def chechIfPalindrome(n):
    '''Check if the number is the same reversed'''

    def reverse_helper(num, reversed_num=0):
        # Base case: when no more digits left
        if num == 0:
            return reversed_num
        
        # Get the last digit
        last_digit = num % 10
        
        # Add this digit to our reversed number
        # Shift reversed_num left by multiplying by 10, then add the digit
        new_reversed = reversed_num * 10 + last_digit
        
        # Remove the last digit from original number and recurse
        return reverse_helper(num // 10, new_reversed)
    return n == reverse_helper(n)
    pass

def main() -> None:
    print(chechIfPalindrome(12221))
    

if __name__ == "__main__":
    main()