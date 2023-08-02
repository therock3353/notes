import heapq

"""
we have k sorted arrays. Each array has n elements. These can be merged into a sorted
array using min-heap.

the problem we will face is how to get next element from the list, this is solved
by using iter() function and saving list_iterators in a different list. this way
we can just call lst_iterator.next() and keep getting next elements from the list.
no need to do index manipulation.

Since we have k arrays, each of size N, total elements in the problem are N*K.
Since each element is added into heap of size k, this adding (or removing) operation is (log(k)).
Hence O(n) = nklog(k)
Memory ~= k since heap is of size k.
"""
def merge_k_sorted_arrays(data):
    result = []
    heap = []
    iterators = [iter(d) for d in data]
    #Create initial heap
    k = len(data)
    index = 0
    while k > 0:
        heapq.heappush(heap, (iterators[index].next(), index))
        k -=1
        index +=1
    # heapq.heapify(heap)
    print "initial heap {}".format(heap)
    #
    while heap:
        entry = heapq.heappop(heap)
        result.append(entry[0])
        it = iterators[entry[1]]
        next_elem = next(it, None)
        if next_elem is not None:
            heapq.heappush(heap, (next_elem, entry[1]))

    return result

if __name__=="__main__":

    data = [
        [10,15,20],
        [5,6,7],
        [4,14,40],
        [2,22,200],
    ]
    print merge_k_sorted_arrays(data)