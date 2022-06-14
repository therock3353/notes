
"""
    https://www.geeksforgeeks.org/check-characters-given-string-can-rearranged-form-palindrome/
    EPI 12.1
    Given a list of characters, can they be rearranged to form a palindrom
"""

def palindrom_permutations(characters):
    char_count_map = {}
    for char in characters:
        if char in char_count_map:
            char_count_map[char] += 1
        else:
            char_count_map[char] = 1

    if len(characters) % 2 == 0:
        for char, count in char_count_map.iteritems():
            if count % 2 != 0:
                return False
        return True
    else:
        one_odd_entry_found = False
        for char, count in char_count_map.iteritems():
            if count % 2 != 0:
                if one_odd_entry_found is True:
                    return False
                else:
                    one_odd_entry_found = True
        return True

if __name__=="__main__":
    chars = "aacc"
    print palindrom_permutations(chars)