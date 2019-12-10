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
