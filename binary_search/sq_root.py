"""
Variant:
    Find the Square root of 300.
"""
def sq_root_normal_method(target):
    index = 1
    #From one check the square of each number
    #1*1=1, 2*2=4, 3*3=9, 4*4=16 ... unless we find the number that is index*index>=target
    while (index*index <target):
        index+=1
    #In this case for target = 300, we will have index=17, 17*17=289, index will be incremented to 18.
    #then the loop exits hence the answer is index-1
    return index-1

print sq_root_normal_method(300)

"""
Calculate the sq root of 300 using binary search approach.
let left = 0 and right be 300 or 150.
mid_pt = (0+150)/2 = 75.
Since 75*75 > 300 then reduce right from 150 to 75

left = 0, right = 75
mid_pt = (0+75)/2 = 37
Since 37*37 > 300 then reduce right from 75 to 37

left = 0, right = 37
mid_pt = (0+37)/2 = 18
Since 18*18 > 300 then reduce right from 37 to 18

left = 0, right = 18
mid_pt = (0+18)/2 = 9
Since 9*9 < 300 then increase left from 0 to 9

left = 9, right = 18
mid_pt = (9+18)/2 = 13
Since 13*13 < 300 then increase left from 9 to 13

left = 13, right = 18
mid_pt = (13+18)/2 = 15
Since 15*15 < 300 then increase left from 13 to 15

left = 15, right = 18
mid_pt = (15+18)/2 = 16
Since 16*16 < 300 then increase left from 15 to 16

left = 16, right = 18
mid_pt = (16+18)/2 = 17
Since 17*17 < 300 then increase left from 16 to 17

.....
.....

"""
def sq_root_binary_search(target):
    left = 0
    right = target/2 #initialize right to target/2. ie if target is 300 then we can safely assume that the sq of 150*150 will never be 300.
    while left<right:
        mid_pt = (left+right)/2
        sq_value = mid_pt*mid_pt
        if sq_value == target:
            return mid_pt
        elif sq_value > target:
            right = mid_pt-1
        else:
            left = mid_pt+1
    return left

print sq_root_binary_search(300)