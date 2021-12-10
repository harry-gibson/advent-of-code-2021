from collections import deque
from statistics import median

with open('./input.txt') as f:
    data = [l.strip() for l in f.readlines()]

openings = ['(', '[', '{', '<']
closings = [')', ']', '}', '>']
pairs = dict((o,c) for o,c in zip(openings, closings))
openings = set(openings)
closings = set(closings)
scores_p1 = {')': 3, ']': 57, '}':1197, '>':25137}
scores_p2 = {')': 1, ']': 2, '}':3, '>':4}

score_p1 = 0
p2_linescores = []
for l in data:
    line_is_corrupt = False
    expected_closings = deque()
    for c in l:
        if c in openings:
            expected_closings.appendleft(pairs[c])
        else:
            assert c in closings
            expected = expected_closings.popleft()
            if expected != c and not line_is_corrupt:
                score_p1 += scores_p1[c]
                line_is_corrupt = True
    if not line_is_corrupt:
        comp_score = 0
        for c in expected_closings:
            comp_score = comp_score * 5 + scores_p2[c]
        p2_linescores.append(comp_score)
score_p2 = median(p2_linescores)

print(f"Part 1: {score_p1}")
print(f"Part 2: {score_p2}")