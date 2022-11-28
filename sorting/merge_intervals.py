'''
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/

    Given overlapping intervals, return unique intervals
    input => [[5, 10], [16, 20], [8, 13], [14, 20]]
    result=> [[5, 13], [14, 20]]

    since we prefer to compare 2 intervals at a time, sort the intervals based on (say) starting time.
             [[5, 10], [16, 20], [8, 13], [14, 20]]
    sorted = [[5, 10], [8, 13], [14, 20], [16, 20]]

    case 1      <------>
                    <------>

    case 2      <-------->
                   <--->

    Time Complexity = O(nlog(n)) + O(n) ~= O(nlog(n))

'''
from operator import itemgetter
def merge_intervals(intervals):
    if not intervals:
        return -1
    if len(intervals) == 1:
        return intervals
    result = []
    intervals = sorted(intervals, key=itemgetter(0))
    print intervals
    result.append(intervals[0])
    for i in range(1, len(intervals)):
        first = result.pop()
        second = intervals[i]
        if first[0] <= second[0] and first[1] >= second[1]:
            result.append(first)
        elif first[0] <= second[0] and second[0] <= first[1]:
            result.append([min(first[0], second[0]), max(first[1], second[1])])
        else:
            result.append(first)
            result.append(second)
    return result

A = [[5, 10], [16, 20], [8, 13], [14, 20]]
A = [[5, 8], [5, 8]]
A = [[10, 20], [30, 40]]
print merge_intervals(A)