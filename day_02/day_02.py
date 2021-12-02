hor = 0
ver = 0
with open('input.txt') as file:
    for line in file:
        direction, amt = line.strip().split()
        amt = int(amt)
        if direction == 'forward':
            hor += amt
        elif direction == 'down':
            ver += amt
        elif direction == 'up':
            ver -= amt
        else:
            assert False, "oops"
print (f"Part 1: {hor * ver}")

hor = 0
ver = 0
aim = 0
with open('./input.txt') as file:
    for line in file:
        direction, amt = line.strip().split()
        amt = int(amt)
        if direction == 'forward':
            hor += amt
            ver += amt * aim
        elif direction == 'down':
            aim += amt
        elif direction == 'up':
            aim -= amt
        else:
            assert False, "oops"
print (f"Part 2: {hor * ver}")