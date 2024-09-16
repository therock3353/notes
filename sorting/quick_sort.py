import random

def random_pivot(st_pt, end_pt):
    random_pivot = random.randint(st_pt, end_pt)
    print "=== Random Index : {} ===".format(random_pivot)
    return random_pivot

def quick_sort(A, start_idx, end_idx):
    pivot_index = (start_idx+end_idx)/2
    element_at_pivot_index = A[pivot_index]
    left = start_idx
    right = end_idx
    while left <= right:
        if A[left] > element_at_pivot_index and A[right] < element_at_pivot_index:
            A[left], A[right] = A[right], A[left]
            left +=1
            right -= 1
        elif A[left] < element_at_pivot_index:
            left+=1
        elif A[right] > element_at_pivot_index:
            right-=1
    A[left+1], A[pivot_index] = A[pivot_index], A[left+1]
    quick_sort(A, start_idx, left)
    quick_sort(A, left+1, end_idx)
    return A


class QuickSort(object):
    def __partition(self, A, start, end):
        pivot = start
        left = start + 1
        right = end
        while True:
            if left <= right and A[right] >= A[pivot]:
                right -= 1
            if left <= right and A[left] >= A[pivot]:
                left += 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
            else:
                break
        A[pivot], A[right] = A[right], A[pivot]
        return right

    def __sort(self, A, start, end):
        if start < end:
            p = self.__partition(A, start, end)
            self.__sort(A, start, p-1)
            self.__sort(A, p+1, end)

    def quicksort(self, A):
        if not A:
            return []
        self.__sort(A, 0, len(A)-1)

if __name__=="__main__":
    d = [8, 2, 5, 3, 4, 1, 6]
    #print quick_sort(d, 0, len(d)-1)
    print QuickSort().quicksort(d)