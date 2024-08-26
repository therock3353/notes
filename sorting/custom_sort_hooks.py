import functools
from operator import attrgetter

class User(object):
    def __init__(self, name):
        self.age = 0
        self.wealth = 0
        self.name = name

    def __repr__(self):
        return "name: {}, age: {}, wealth {}".format(self.name, self.age, self.wealth)


def custom_sorter(object):
    return object.age * object.wealth

'''
179. Largest Number
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"

My example:
    [2, 8, 44, 46, 81]
    
    In this example: 
        - 46 should come before 44
        - 8 should come before 81
    
    so when comparing 46(a) with 44(b) if "46"+"44" > "44"+"46" = "4644" > "4446" then a is ahead of b.
    similarly:
        comparing 8(a) with 81(b) => "8"+"81" = "881" > "81"+"8" = "818"
'''
def find_largest_number(nums):
    if not nums:
        return ""

    def custom_sort(a, b):
        if a+b > b+a:
            return 1
        elif b+a > a+b:
            return -1
        else:
            return 0

    nums = [str(i) for i in nums]
    sorted_nums = sorted(nums, key=functools.cmp_to_key(custom_sort), reverse=True)
    return ''.join(sorted_nums)


if __name__=="__main__":
    u1 = User("A")
    u1.age = 10
    u1.wealth = 100
    u2 = User("B")
    u2.age = 20
    u2.wealth = 200
    u3 = User("C")
    u3.age = 40
    u3.wealth = 40
    users = [u1, u2, u3]
    ''' Sort by age '''
    print(sorted(users, key=attrgetter('age')))
    ''' Sort by wealth '''
    print(sorted(users, key=attrgetter('wealth'), reverse=True))
    ''' Sort by custom rule 2*age + 3*wealth '''
    print(sorted(users, key=lambda x: custom_sorter(x)))

    nums = [2, 81, 40, 9, 44, 8]
    print(find_largest_number(nums))