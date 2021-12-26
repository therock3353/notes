from copy import deepcopy


def is_palindrom(word):
    if len(word) == 1:
        return True
    left = 0
    right = len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1

    return True


def dfs(candidate, remaining, result, results):
    if not remaining:
        results.append(deepcopy(result))
        return

    for i in range(len(remaining)):
        candidate += remaining[i]
        if not is_palindrom(candidate):
            continue
        dfs("", remaining[i+1:], result+[candidate], results)

def palindrom_partition(palindromic_str):
    results = []
    dfs(candidate="", remaining=palindromic_str, result=[], results=results)
    return results


if __name__=="__main__":
    word = "apaphh"
    for r in palindrom_partition(word):
        print(r)