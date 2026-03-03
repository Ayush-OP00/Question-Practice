#program to print all even numbers from a given list of numbers in the same order and stop printing any after 237 in the sequence.

def even(num):

    if num%2 ==0:
        return num
    
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
result = numbers[0: numbers.index(237) + 1]#number.index : gives the index of the first occurrence of 237 in the list. The slice [0: numbers.index(237) + 1] creates a new list that includes all elements from the start of the original list up to and including (because of +1) the element at the index of 237.
print (result)
