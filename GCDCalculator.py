#program that computes the greatest common divisor (GCD) of two positive integers.

def gcd(a, b):
    
    gcd = 1

    if a % b == 0:  # If a is divisible by b, then b is the GCD.
        return b
    
    # Iterate from half of b down to 1.

    for k in range(int(b / 2), 0, -1): 
        #range() function generates numbers for the loop: range(start, stop, step). 
        # Loop counts backwards.
        #-1 means: Decrement the loop variable k by 1 in each iteration, effectively counting downwards.
        # Check if both a and b are divisible by k.
        if a % k == 0 and b % k == 0:
            # Update the GCD to the current value of k and exit the loop.
            gcd = k
            break
    
    # Return the calculated GCD.
    return gcd

num1 = int(input("Enter the first positive integer: "))
num2 = int(input("Enter the second positive integer: "))
result = gcd(num1, num2)
print("The GCD of", num1, "and", num2, "is", result)