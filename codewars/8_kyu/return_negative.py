#   https://www.codewars.com/kata/55685cd7ad70877c23000102/train/python
'''
In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?
'''
def make_negative( number ):
    if number > 0:
        newnum = number * -1
        return newnum
    else:
        return number