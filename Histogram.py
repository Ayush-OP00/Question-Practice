#Python program to create a histogram from a given list of integers.

def histogram(items):

    for n in items:
        output = ''
        times = n

        while(times > 0):
            output += '*' 
            #outtput = output + '*' 
            times = times - 1
        print(output)
    
numbers = [int(x) for x in input("Enter a list of integers: ").split()]
histogram(numbers)

            