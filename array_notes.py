"""
    range(st_pt, end_pt) : range(0, 10) will print 0-9 not including 10
"""
d = ['a', 'b', 'c']
for i in range(len(d)):
    print i #this will print 0,1,2 as length is 3

for i in reversed(range(len(d))):
    print i #this will print 2,1,0

#     0,   1,   2,   3,   4
d = ['a', 'b', 'c', 'd', 'e']
print d[:1]
print d[1:]
print d[1:3] #['b', 'c']
"""
In slicing data[st_pt: end_pt] element at st_pt is included but element at end_pt is not included.
Example:
    d[1:3] --> element at index 1 which is b is included but element at index 3 which is 'd' is not included
    d[:1] --> all elements upto index 1 but not including 1
    d[1:] --> all elements starting from index 1 including element at index 1
"""

'''
In python arrays, slicing by indexing is very good. You don't get index error.

'''
data = [10,20]
print data[5:] #print data from index 5 onwards. There is no index 5 so it will print empty list but no index error
data = []
print data[:1] #print data till (not including) index 1. But list only has 1 element (index 0) still no index error is thrown.
#only empty list is created.


'''
    Calculate power to operation
    10^2 = 100 (10 raised to 2 = 100). In python this would be 10 ** 2 = 100
'''

'''
    Mod operator in python is %
    Mod means "baki" in marati.
    print "8 % 3 =", 8 % 3 #2
    print "5 % 2 =", 5 % 2 #1
    
'''


'''
    reverse a string:
        x = "this"
        x = x[::-1] would reverse the string
'''


'''
    a = [5, 4, 2, 10]
    a.sort() will sort the list but the operation sorts in-place and returns nothing
    print a.sort() will print None so x = a.sort(), x is None

    sorted(a) on the other hand returns a list
    x = sorted(a), x = sorted list of a elements
'''