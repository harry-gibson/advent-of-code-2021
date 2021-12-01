import numpy as np

infile = 'input.txt'
data = np.recfromtxt(infile)

# Part 1: find how many times the value increases from the previous
increases = data[1:] > data[:-1]
res = np.sum(increases)
print(f"The answer to Day 1 Part 1 is {res}")

# Part 2: find how many times the sum of a moving window of size 3 increases
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

# NB: subsequently others pointed out that we don't need to sum the whole moving window,
# we can just compare the first val in the window with the last val in the prev window,
# if the one that has "just left" is less than the one that has "just entered" then the 
# sum will have increased. So we can do part 2 much more simply:

increases_2 = data[3:] > data[:-3]
res_2b = np.sum(increases_2)
print(f"The more efficient answer to Day 1 Part 2 is {res_2b}")

