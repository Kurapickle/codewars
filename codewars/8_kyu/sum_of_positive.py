#   https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python
'''
You get an array of numbers, return the sum of all of the positives ones.
'''
def positive_sum(arr):
    parr=[]
    for n in arr:
        if n >=0:
            parr.append(n)
            
    return sum(parr)