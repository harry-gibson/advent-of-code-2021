import numpy as np

data = np.genfromtxt('input.txt', delimiter=1)

powers = 2 ** np.arange(data.shape[-1])[::-1]

# Part 1
means = data.mean(axis=0)
gamma_binary = means >= 0.5
eps_binary = means < 0.5

part1 = (gamma_binary.dot(powers)) * (eps_binary.dot(powers))
print(f"Part 1 answer: {part1}")

# Part 2

def filter(in_arr, op, col_pos=0):
    if in_arr.shape[0]==1 or col_pos == in_arr.shape[1]-1:
        return in_arr
    most_common = op(in_arr[:, col_pos].mean(), 0.5)
    filtered = in_arr[in_arr[:, col_pos]==most_common]
    return filter(filtered, op, col_pos+1)

oxygen = filter(data, np.greater_equal)
co2 = filter(data, np.less)

part2 = ((oxygen.dot(powers)) * co2.dot(powers)) [0]
print(f"Part 2 answer: {part2}")
