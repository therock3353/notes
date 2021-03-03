
"""
    Input is a sequence and you have to produce all permutations of the input sequence.
    [2,5,10] is input then
        => [2,5,10],[2,10,5],[5,2,10],[5,10,2],[10,5,2],[10,2,5]
"""

"""
                                            [2,5,10]
                                                |
                    ----------------------------------------------------------------
                    |                           |                                   |
                [2] [5,10]                    [5] [2,10]                        [10][2,5]
            selected | remaining                 |                                   |
        -------------------                 -----------------                  ---------------------
        |                  |                |               |                  |                    |
    [2,5] [10]          [2,10][5]       [5,2][10]        [5,10][2]          [10,2][5]           [10,5][2]
selected   remaining                                   selected  remaining


    for i in range(len(remaining)):
        selected = selected + remaining[i] => at each iteration, select an element and add to selected


"""


def permutations(selected, remaining, result, input_len):
    if len(selected) == input_len:
        result.append(selected)
        return

    for i in range(len(remaining)):
        permutations(selected=selected+[remaining[i]],
                     remaining=remaining[:i]+remaining[i+1:],
                     result=result,
                     input_len=input_len)

    return result


if __name__=="__main__":
    d = [2,5,10]
    print permutations([],d,[],len(d))