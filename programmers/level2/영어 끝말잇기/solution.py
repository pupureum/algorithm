def solution(n, words):
    db = [words[0]]
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0]:
            return [(i % n) + 1, (i // n) + 1]
        else:
            if words[i] in db:
                return [(i % n) + 1, (i // n) + 1]
            db.append(words[i])
    return [0,0]

words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(3, words))