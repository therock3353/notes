"""
EPI 12.11 -> Students with TOP 3 scores

You are given input like ->
    scores = [['Student1', 10, 30, 45, 32, 80],
              ['Student2', 60, 50, 55, 32, 82],
              ['Student3', 80, 60, 65, 66, 84], #84, 80, 66 = 76.6
              ['Student4', 90, 50, 75, 32, 60], #90, 75, 60 = 75
              ['Student5', 70, 40, 85, 66, 66], #85, 70, 66 = 73
              ['Student6', 50, 30, 95, 32, 30],
              ['Student7', 50, 40, 45, 38, 81]
               ...
               ...
              ]

    for each student take their top 3 scores from a list of scores. Take avg of these top 3 scores.
    calculate top 3 students based on above calculations.

    Brute Force:
    ===========
    student_score_map = {}
    for student in students:
        score.sort() #if there are m scores then mlog(m)
        avg_score = avg(score[0:3])
        student_score_map[student_id] = avg_score

    sort(student_score_map) based on marks. #if there are n students then nlog(n)

    time complexity: n*(mlog(m)) + nlog(n). if m is small compared to n (10000 students each with 10 marks)
    then we can ignore mlog(m). so O => n + nlog(n) ~= 2nlog(n)

    space complexity: n

    Using Min-Heap:
    student_marks_heap = []
    for student in students:
        #using min-heap get top 3 scores
        #time complexity will be mlog(k)
        avg_score = calc_avg_score(score_heap[0:3])
        #using min-heap calculate top 3 students with highest avg_marks
        heapq.heappush(student_marks_heap, avg_score)
        #operational complexity nlog(k)

    time complexity: mlog(k) + nlog(k). If k is small, log(k) can be ignored. if n >> m then m can be ignored.
    hence O => n
    space complexity: k
"""

import heapq
def top_student_scores(scores, k):
    if not scores or not k:
        return
    top_student_heap = []
    for i in range(len(scores)):
        top_marks_heap = []
        for j in range(1, k+1):
            top_marks_heap.append(scores[i][j])
        heapq.heapify(top_marks_heap)
        for j in range(k+1, len(scores[i])):
            root_elem = heapq.heappop(top_marks_heap)
            if scores[i][j] > root_elem:
                heapq.heappush(top_marks_heap, scores[i][j])
            else:
                heapq.heappush(top_marks_heap, root_elem)
        total_marks = 0
        for marks in top_marks_heap:
            total_marks += marks
        avg_marks = total_marks/k
        if i < k:
            heapq.heappush(top_student_heap, (avg_marks, scores[i][0]))
        else:
            root_elem = heapq.heappop(top_student_heap)
            if avg_marks > root_elem[0]:
                heapq.heappush(top_student_heap, (avg_marks, scores[i][0]))
            else:
                heapq.heappush(top_student_heap, root_elem)

    top_students = []
    while top_student_heap:
        top_students.append(heapq.heappop(top_student_heap)[1])
    top_students.reverse()

    return top_students

if __name__=="__main__":
    scores = [['Student1', 10, 30, 45, 32, 80],
              ['Student2', 60, 50, 55, 32, 82],
              ['Student3', 80, 60, 65, 66, 84], #84, 80, 66 = 76.6
              ['Student4', 90, 50, 75, 32, 60], #90, 75, 60 = 75
              ['Student5', 70, 40, 85, 66, 66], #85, 70, 66 = 73
              ['Student6', 50, 30, 95, 32, 30],
              ['Student7', 50, 40, 45, 38, 81]
              ]
    print top_student_scores(scores, 3)
