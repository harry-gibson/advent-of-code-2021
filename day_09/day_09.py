import numpy as np

data = np.genfromtxt('./input.txt', delimiter=1).astype(int)
padded = np.pad(data, (1), mode='constant', constant_values=np.iinfo(data.dtype).max)
# create 4 arrays where at each location, the pixel value is that of the input array's neighbour
# to the (s,n,w,e)
below = np.roll(padded, -1, axis=0)
above = np.roll(padded, 1, axis=0)
left = np.roll(padded, 1, axis=1)
right = np.roll(padded, -1, axis=1)
# a cell is a sink if it is lower than any of the four neighbour cells
nbr_mins = np.stack((below, above, left, right)).min(axis=0)
sinks = (padded < nbr_mins).astype(int)
print(f"Part 1: {sinks.sum() + (padded * sinks).sum()}")



# The data has 9s marking the watershed lines so the "basins" are not connected and therefore 
# we can do connected component analysis, i.e. we find connected regions in a mask of 
# `data != 9`. We don't need to use the sink point from part 1. Use scipy.
from scipy.ndimage.measurements import label
labels, _ = label(data != 9)
basin_ids, basin_sizes = np.unique(labels, return_counts=True)

# the background, zero, i.e. locations where the data was 9, is zero in the basin ids map
# there are likely more of this than any other value (but we shouldn't rely on that being 
# the case and just take the 1:3 most common). So remove count of 9-pixels.
basin_id_0_idx = np.argwhere(basin_ids==0)
basin_sizes[basin_id_0_idx] = 0
three_largest_basin_sizes = sorted(basin_sizes, reverse=True)[:3]
print(f"Part 2: {np.prod(three_largest_basin_sizes)}")