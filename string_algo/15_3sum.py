
'''
    The operational complexity is ~ O(n^3)
          N-2
        ----
        \     (n-1)*(n-2)
        |
        ----
         n=0
'''

def sum_brute_force(seq):
    if not seq:
        return None
    i = 0
    result = []
    for i in range(len(seq)-2):
        for j in range(i+1, len(seq)-1):
            for k in range(j+1, len(seq)):
                if seq[i] + seq[j] + seq[k] == 0:
                    result.append((seq[i], seq[j], seq[k]))
    return result

'''
    s = [-4, 2, 1, 3, 8, -5]
    s.sort()
    s = [-5, -4, 1, 2, 3, 8]
    
    [-5, -4, 1, 2, 3, 8]
      i    l           r
    [-5, -4, 1, 2, 3, 8]
      i      l         r
    [-5, -4, 1, 2, 3, 8]
      i       l    r   
    [-5, -4, 1, 2, 3, 8]        => found pair
      i         l  r   

    [-5, -4, 1, 2, 3, 8]
          i  l        r
    [-5, -4, 1, 2, 3, 8]        => found pair
          i  l     r   

    [-5, -4, 1, 2, 3, 8]
             i  l     r



'''

def three_sum(seq):
    if not seq:
        return None
    seq.sort()  # O(nlog(n))
    result = []
    for i in range(len(seq)-2):
        left = i + 1
        right = len(seq)-1
        required_sum = -1 * seq[i]
        while left < right:
            if seq[left]+seq[right] == required_sum:
                result.append((seq[i], seq[left], seq[right]))
                left += 1
                right -= 1
            elif seq[left]+seq[right] > required_sum:
                right -= 1
            else:
                left += 1

    return result

if __name__=="__main__":
    s = [-4, 2, 1, 3, 8, -5]
    print(sum_brute_force(s))
    print(three_sum(s))