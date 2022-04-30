#   https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python
'''
Given an array of integers.
Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.
 0 is neither positive nor negative.
If the input is an empty array or is null, return an empty array.
'''
def count_positives_sum_negatives(arr):
    pos=0
    neg=0
    
    if len(arr) == 0:
        return[]
        
    for num in arr:
        if num > 0:
            pos+=1
        else:
            neg+=num
    
    return [pos, neg]