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

# A = [[5, 10], [16, 20], [8, 13], [14, 20]]
# A = [[5, 8], [5, 8]]
# A = [[10, 20], [30, 40]]
# print merge_intervals(A)


'''
252. Meeting Rooms
Given an array of meeting time intervals where intervals[i] = [starti, endi], 
determine if a person could attend all meetings.

'''

def canAttendMeetings(intervals):
    if not intervals:
        return False
    if len(intervals) == 1:
        return True
    i = 0
    intervals = sorted(intervals, key=itemgetter(0))
    while i < len(intervals)-1:
        if intervals[i+1][0] < intervals[i][1]:
            return False
        i += 1
    return True

# A = [[5, 10], [16, 20], [8, 13], [14, 20]]
# A = [[5, 8], [5, 8]]
# A = [[10, 20], [30, 40]]
# print canAttendMeetings(A)


'''
253. Meeting Rooms II
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of conference rooms required.
https://leetcode.com/problems/meeting-rooms-ii/
'''
import heapq
def minMeetingRooms(intervals):
    if not intervals:
        return -1
    max_num_rooms = 1
    curr_num_rooms = 1
    ending_times = []
    intervals = sorted(intervals, key=itemgetter(0))
    heapq.heappush(ending_times, intervals[0][1])
    for i in range(1, len(intervals)):
        if ending_times:
            curr_end_time = heapq.heappop(ending_times)
        else:
            heapq.heappush(ending_times, intervals[i][1])
            curr_num_rooms = 1
            continue
        if intervals[i][0] < curr_end_time:
            curr_num_rooms += 1
            heapq.heappush(ending_times, curr_end_time)
            heapq.heappush(ending_times, intervals[i][1])
        else:
            curr_num_rooms = max(1, curr_num_rooms)
            heapq.heappush(ending_times, intervals[i][1])
        if curr_num_rooms > max_num_rooms:
            max_num_rooms = curr_num_rooms
    return max_num_rooms

A = [[1,8],[6,20],[9,16],[13,17]]
#A = [[1, 4], [5, 8], [6, 9]]
print minMeetingRooms(A)