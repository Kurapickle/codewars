#   https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python

'''
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items.
 We want to create the text that should be displayed next to such an item.
Implement the function which takes an array containing the names of people that like an item.
 It must return the display text as shown in the examples:
'''
def likes(names):
    if len(names) == 0:
        print ("no one likes this")
    elif len(names) == 1:
        print (f"{names[0]} likes this")
    elif len(names) == 2:
        print (f"{names[0]} and {names[1]} likes this")
    elif len(names) == 3:
        print(f"{names[0]}, {names[1]} and {names[2]} likes this")
    elif len(names) > 3:
        print(f"{names[0]}, {names[1]} and {len(names)-2} likes this")


