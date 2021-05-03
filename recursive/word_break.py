"""
                                    "iamace"
            ----------------------------------------------------------------------------------
            |                   |               |               |               |             |
        i : amace             ia: mace      iam: ace        iama: ce        iamac: e        iamace
             |
    ------------------------
    |               |
    a : mace      am: ace
        |               |
        |               |
    --------------------V------------------
    |               |   |        |         |
    m : ace(X)     ma : ce(X)  mac: e(X)  mace(X)
                        V
                        |
                    -----------------------------
                    |              |            |
                   a: ce          ac: e(X)      ace
                       |
                    ---------------
                    c: e (X)    ce(X)

"""



l = ['i', 'am', 'ace', 'a']
DICTIONARY = set(l)

def word_break(s, result=False):
    if not s:
        return False

    for i in range(len(s)):
        wrd = s[:i+1]
        if wrd in DICTIONARY:
            if i == len(s)-1:
                result = True
            else:
                result = word_break(s[i+1:])
        else:
            result = False
        if result is True:
            break

    return result


if __name__=="__main__":
    s = "iamace"
    s = "catsanddog"
    print word_break(s, False)