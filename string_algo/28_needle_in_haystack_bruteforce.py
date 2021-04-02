"""
    Substring Search:
    Text: abdacdagoa
    Pattern: dag

    |a|b|d|a|c|d|a|g|o|a|
     ^
    |d|a|g
     ^
    ======
    |a|b|d|a|c|d|a|g|o|a|
       ^
      |d|a|g
       ^
    ======
    |a|b|d|a|c|d|a|g|o|a|
         ^
        |d|a|g
         ^

    |a|b|d|a|c|d|a|g|o|a|
           ^
        |d|a|g
           ^

    |a|b|d|a|c|d|a|g|o|a|
             ^
        |d|a|g   c != g hence no substr
             ^
    =======
    |a|b|d|a|c|d|a|g|o|a|
           ^
          |d|a|g
           ^
    =======
    |a|b|d|a|c|d|a|g|o|a|
             ^
            |d|a|g
             ^
    =======
    |a|b|d|a|c|d|a|g|o|a|
               ^
              |d|a|g
               ^
    |a|b|d|a|c|d|a|g|o|a|
                 ^
              |d|a|g
                 ^
    |a|b|d|a|c|d|a|g|o|a|
                   ^
              |d|a|g    MATCH
                   ^

If len(text) == n and len(pattern) == m then Operation Complexity
of this approach is (n-m) * m ~= n*m (if n is much larger than m)

"""


def is_substr(text, pattern):
    if not text or not pattern:
        return False
    if len(pattern) > len(text):
        return False

    is_substr_present = False
    text_index = 0
    while is_substr_present is False and text_index < len(text):
        pattern_index = 0
        index = text_index
        while index < len(text) and pattern_index < len(pattern) and text[index] == pattern[pattern_index]:
            index += 1
            pattern_index += 1
        if pattern_index == len(pattern):
            is_substr_present = True
            break
        text_index += 1

    return is_substr_present

if __name__=="__main__":
    text = "abfnnufewfnnclnf"
    needle = "clnf"
    print is_substr(text, needle)