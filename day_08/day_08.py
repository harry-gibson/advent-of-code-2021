# Part 1

n_1478 = 0
with open('./input.txt') as f:
    for line in f.readlines():
        output = line.split(' | ')[1].strip()
        words = output.split(' ')
        n_1478 += sum([1 for w in words if len(w) in [2,3,4,7]])
print(f"Part 1: {n_1478}")

'''
THINGS WE KNOW

Digits : n_segments they use
0 : 6 
1 : 2 
2 : 5 
3 : 5 
4 : 4 
5 : 5 
6 : 6 
7 : 3 
8 : 7 
9 : 6 

Digits : segment letters they use with normal wiring
0 : abcefg
1 : cf
2 : acdeg
3 : acdfg
4 : bcdf
5 : abdfg
6 : abdefg
7 : acf
8 : abcdefg
9 : abcdfg

Total times each segment is used across digits 0:9:
a: 8
b: 6
c: 8
d: 7
e: 4
f: 9
g: 7
'''

def find_segment_mapping(words):
    '''Returns dictionary mapping the current segment id to what it should be'''
    allchars = ''.join(words)
    charset = set(allchars)
    
    digit7 = [w for w in words if len(w) == 3][0]
    digit1 = [w for w in words if len(w) == 2][0]
    seg_a = [c for c in digit7 if c not in digit1][0]
    
    seg_b = [c for c in charset if allchars.count(c) == 6][0]
    seg_e = [c for c in charset if allchars.count(c) == 4][0]
    seg_f = [c for c in charset if allchars.count(c) == 9][0]
    
    digit4 = [w for w in words if len(w) == 4][0]
    seg_d = [c for c in digit4 if c not in digit1 and c != seg_b][0]
    
    seg_c = [c for c in charset if allchars.count(c) == 8 and c != seg_a][0]
    seg_g = charset.difference(set([seg_a,seg_b,seg_c, seg_d, seg_e, seg_f])).pop()
    
    return {
        seg_a: 'a', seg_b: 'b', seg_c: 'c', seg_d: 'd', seg_e: 'e', seg_f: 'f', seg_g: 'g'
    }

DIGITS = {
    'abcefg': '0', 'cf': '1', 'acdeg': '2', 'acdfg': '3', 'bcdf': '4',
    'abdfg': '5', 'abdefg': '6', 'acf': '7', 'abcdefg': '8', 'abcdfg': '9'
}

def translate_digit(digit_word, mapping):
    translated_word = [mapping[c] for c in digit_word]
    return DIGITS[''.join(sorted(translated_word))]

total = 0
with open('./input.txt') as f:
    for line in f.readlines():
        in_maps, in_digits = [p.split(' ') for p in line.strip().split(' | ')]
        mapping = find_segment_mapping(in_maps)
        total += int(''.join([translate_digit(d, mapping) for d in in_digits]))
print(f"Part 2: {total}")