#   https://www.codewars.com/kata/5ab6538b379d20ad880000ab/train/python
'''
You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square.
If it is a square, return its area. If it is a rectangle, return its perimeter.

area_or_perimeter(6, 10) --> 32
area_or_perimeter(3, 3) --> 9
'''
def area_or_perimeter(l , w):
    if l == w:
        area = l * l
        return(area)
    else:
        perimeter = l + l + w + w 
        return(perimeter)