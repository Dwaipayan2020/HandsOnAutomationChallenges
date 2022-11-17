"""2> 1.
d = {1= 1, 2= 2}   ----------------> returns invalid syntax
print(d)
"""

"""2> 4.
d = {1= 1, 2= 2}   
print(d)
"""
# d = {(1, 2), (2, 2)} ---> Works as a set


# d = dict([(1, 2), (2, 3)])        ---> returns {1: 2, 2: 3} as dictionary
# d = dict(((1, 2), (2, 3)))        ---> returns {1: 2, 2: 3} as dictionary
# 2>10. d = dict(x=2, y=3)          ---> returns {'x': 2, 'y': 3} as dictionary

# 2>5. d = {'a': 'A', c: [1234]}    -- > Throws name error
# 2>11. d = dict('x'=2, 'y'=3)          ----> Throws SyntaxError: expression cannot contain assignment
# 2>12. d = dict(1=2, 2=3)          ----> Throws SyntaxError: expression cannot contain assignment

d = dict([('x', 2), ('y', 3)])
