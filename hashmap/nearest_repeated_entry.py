"""
EPI 12.4
 if s = ["a", "b", "c", "d", "b", "c", "m", "c"]
          0    1    2    3    4    5    6    7
    c at 5th and 7th location is most near each other.
    and distance between them is 7-5 = 2

      
"""

def nearest_repeated_entry(data):
    if not data:
        return -1
    min_dist_between_repeated_words = float('inf')
    word_index_map = {}
    for i in range(len(data)):
        if data[i] not in word_index_map:
            word_index_map[data[i]] = i
        else:
            previous_index = word_index_map.get(data[i])
            if min_dist_between_repeated_words > (i - previous_index):
                min_dist_between_repeated_words = i - previous_index
            word_index_map[data[i]] = i

    return min_dist_between_repeated_words if min_dist_between_repeated_words != float('inf') else -1

if __name__=="__main__":
    seq = ["a", "b", "c", "d", "b", "c", "m", "c"]
        #   0    1    2    3    4    5    6    7
    print nearest_repeated_entry(seq)