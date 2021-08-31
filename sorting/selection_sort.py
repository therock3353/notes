
"""
    https://www.hackerearth.com/practice/algorithms/sorting/selection-sort/tutorial/

    For each iteration

    d = [2,5,1,3,2,8,4]

     i  max_so_far
     |  |
    [2, 5, 1, 3, 2, 8, 4]
                      far_right

       max_so_far
        |     i
    [2, 5, 1, 3, 2, 8, 4]
                      far_right

       max_so_far
        |        i
    [2, 5, 1, 3, 2, 8, 4]
                      far_right

                max_so_far
                    |
    [2, 5, 1, 3, 2, 8, 4]
                      far_right


    The difference between selection sort and bubble sort is that in selection sort, for each iteration, we select the highest
    element and swap it with far right position. In bubble sort, we take the largest element and keep swapping it with it's neighbour
    untill it goes to far right (bubbles up).

    Selection Sort
            Best Case : O(n^2)
            Avg Case : O(n^2)
            Worst Case : O(n^2)


"""
def selection_sort(A):
    largest_element_pos = len(A)-1
    for _ in range(len(A)):
        i = 0
        index_of_largest_elem_so_far = 0
        while i < largest_element_pos:
            if A[i] > A[index_of_largest_elem_so_far]:
                index_of_largest_elem_so_far = i
            i+=1
        A[index_of_largest_elem_so_far], A[largest_element_pos] = A[largest_element_pos], A[index_of_largest_elem_so_far]
        largest_element_pos-=1
    return A

if __name__=="__main__":
    d = [2,5,1,3,2,8,4]
    print selection_sort(d)