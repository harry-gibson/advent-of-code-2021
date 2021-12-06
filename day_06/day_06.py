import numpy as np

fish_master = np.fromfile('./input.txt', sep=',').astype(int)

# PART 1
fish = fish_master.copy()
days = 0
sprogging = fish==0
while days < 80:
    n_sprogging = np.count_nonzero(sprogging)
    fish -= 1
    fish[sprogging] = 6
    sprogs = np.array([8] * n_sprogging)
    fish = np.concatenate((fish, sprogs))
    sprogging = fish==0
    days += 1
print(f"Part 1: After {days} days there are {len(fish)} fish")

# PART 2

# Brute-forcing it by running part 1 to 256 days is not feasible
initial_age_counts =  np.unique(fish_master, return_counts = 1)
age_counts =  [0]*9
for i, age in enumerate(initial_age_counts[0]):
    if age in initial_age_counts[0]:
        age_counts[age] = initial_age_counts[1][i]
    else:
        age_counts[age] = 0

days = 0
while days < 256:
    n_sprogging = age_counts.pop(0)
    age_counts[6] += n_sprogging
    age_counts.append(n_sprogging)
    days += 1
print(f"Part 2: After {days} days there are {sum(age_counts)} fish")