import numpy as np

infile = 'input.txt'
data = np.recfromtxt(infile)

increases = data[1:] > data[:-1]
res = np.sum(increases)
print(f"The answer to Day 1 Part 1 is {res}")

window_size = 3
strided_shape = data.shape[:-1] + (data.shape[-1] - window_size + 1, window_size)
window_strides = data.strides + (data.strides[-1],)

moving_windows = np.lib.stride_tricks.as_strided(
    data, 
    shape=strided_shape, 
    strides=window_strides)
window_sums = np.sum(moving_windows, axis=-1)
window_increases = window_sums[1:] > window_sums[:-1]
res_2 = np.sum(window_increases)
print(f"The answer to Day 1 Part 2 is {res_2}")