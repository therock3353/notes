"""
    Operational complexity of this approach is similar to DP approach m*n.

    s1 = "abaecdefg"
    s2 = "mcdeq"

    "a b a e c d e f g"
    "m c d e q"             lcs = ""

    "a b a e c d e f g"
      "m c d e q"           lcs = ""

    "a b a e c d e f g"
        "m c d e q"         lcs = ""

    "a b a e c d e f g"
          "m c d e q"       lcs = "cde"
             -----

    "a b a e c d e f g"
            "m c d e q"     lcs = ""

    "a b a e c d e f g"
              "m c d e q"   lcs = ""

    "a b a e c d e f g"
                "m c d e q"    lcs = ""

    "a b a e c d e f g"
                  "m c d e q"  lcs = ""

    "a b a e c d e f g"
                    "m c d e q"  lcs = ""

"""
def calculate_current_lcs(s1, s2, s1_index):
    lcs = ""
    current_lcs = ""
    index1 = s1_index
    index2 = 0
    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] == s2[index2]:
            current_lcs += s1[index1]
        else:
            if len(current_lcs) > len(lcs):
                lcs = current_lcs
            current_lcs = ""
        index1 += 1
        index2 += 1
    return lcs

def longest_common_substr_brute_force(s1, s2):
    lcs = ""
    for i in range(len(s1)):
        current_lcs = calculate_current_lcs(s1, s2, i)
        if len(current_lcs) > len(lcs):
            lcs = current_lcs
    return lcs

if __name__=="__main__":
    s1 = "abaecdefg"
    s2 = "mcdeq"
    print longest_common_substr_brute_force(s1, s2)