
"""
Think of insertion sort like you have few cards (patte) in hand. You would have sorted them
according to some order in hand, when you pick a new card from a deck of cards, you will
place that card somewhere in the middle according to the cards you have.

Implementation logic:
    i
[8, 2, 5, 3, 4, 1, 6]

Compare all items till i and make sure they are sorted.
i.e A[0] and A[1] => [2, 8....]

        i
[2, 8, 5, 3, 4, 1, 6]
    <--
imagine now you have 5 to place in [2,8] array. So compare 5 with existing elements in hand.
[2,5,8 ...]

          i
[2, 8, 5, 3, 4, 1, 6]
        <--
imagine now you have 3 to place in [2,5,8] array. So compare 3 with existing elements in hand.
[2,3,5,8 ...]

             i
[2, 8, 5, 3, 4, 1, 6]
           <--
imagine now you have 4 to place in [2,3,5,8] array. So compare 4 with existing elements in hand.
[2,3,4,5,8 ...]


# Best Case O(n):
# if input is already sorted [1,2,3,4] then all you have to do is go through the array and do (n)
# comparisions.
# Worst Case O(n^2):
#   1+2+3+...(n-1) = (n*(n-1))/2 = O(n^2)
# -----------------
# Average Case O(n^2):
# ------------------
# Average and Worst case are same.
"""
def insertion_sort(A):
    if not A:
        return []

    for i in range(1, len(A)):
        while i>0 and A[i]<A[i-1]:
            A[i], A[i-1] = A[i-1], A[i]
            i-=1
    return A

if __name__=="__main__":
    d = [8, 2, 5, 3, 2, 4, 1, 6]
    print insertion_sort(d)