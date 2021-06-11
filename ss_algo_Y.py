def groupwords(words):
    def keybyword(word):
        return ''.join(sorted(word))

    groups = {}
    for word in words:
        groupkey = keybyword(word)
        if groupkey not in groups:
            groups[groupkey] = []
        groups[groupkey]. append(word)
    ans = []
    for groupkey in groups:
        ans.append(groups[groupkey])
    return ans