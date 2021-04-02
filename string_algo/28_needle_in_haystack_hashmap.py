"""
    Substring Search:
    Text: abdacdagoa
    Pattern: dag

    Go through the text and create all possible substrings of text of size pattern.
    Example: abd, bda, dac, acd, cda, dag, ago, goa are all substrings of text abdacdagoa
    of length 3 (because dag is of length 3)

    Now we store all these in a set and find if pattern exists or not.

    Time Complexity is O(n)  ==> The set look-up is O(1) but we still need O(n) to populate set
    Space Complexity is O(n) ==> If text is of length 10 and we need to split it into chunks of 3 then the last
                                chunk will start at index 8 hence there are (n-m) + 1 such chunks.
                                If n >> m then we can say that there are n chunks.

"""
def is_substr(text, pattern):
    if not text or not pattern:
        return False
    if len(pattern) > len(text):
        return False
    is_substr_present = False
    unique_substrs = set()
    start_pt = 0
    end_pt = start_pt
    while end_pt < len(text):
        end_pt = start_pt + len(pattern)
        substr = text[start_pt: end_pt]
        unique_substrs.add(substr)
        start_pt += 1

    if pattern in unique_substrs:
        is_substr_present = True
    return is_substr_present


if __name__=="__main__":

    text = "abfnnufewfnnclnf"
    needle = "xcd"
    print is_substr(text, needle)