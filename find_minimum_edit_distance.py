def find_minimum_edit_distance(word1:str,word2:str)->int:
    # we will convert one word to another and compute the cost along the way
    word1 = word1.lower()
    word2 = word2.lower()
    word1 = list(word1)
    word2 = list(word2)
    # make lengths equal
    diff = len(word1) - len(word2)
    if diff > 0:
        for i in range(diff):
            word2.append('')
    elif diff < 0:
        for i in range(abs(diff)):
            word1.append('')
    # first find all matching items and swap
    for char2 in word2:
        for char1 in word1:
            if char1 == char2:
                temp = word1[word2.index(char2)] #  word1[word2.index(char2)]
                word1[word1.index(char1)] = temp
                word1[word2.index(char2)] = char2
                continue
    # now delete or insert
    # includes cost
    cost = 0
    for char2,char1 in zip(word2,word1):
            if char1 == '':
                word1[word1.index("")] = char2
                cost = cost + 1
            elif char1 != char2:
                word1[word1.index(char1)] = char2
                cost = cost + 2
    return cost
