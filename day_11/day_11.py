import numpy as np

NBR_OFFSETS = (np.indices([3, 3])-1).T.reshape(9,2)
NBR_OFFSETS = np.delete(NBR_OFFSETS, 4, axis=0)

data = np.genfromtxt('./input.txt', delimiter=1).astype(np.int_)

def octo_step(octogrid):
    grid_shape = octogrid.shape[0]
    assert grid_shape == octogrid.shape[1]  # if not, handle it in the coord bounds check below
    energy_lvls = octogrid + 1
    now_flash_coords = np.argwhere(energy_lvls > 9)
    just_flashed_mask = np.zeros_like(energy_lvls)
    n_flashes = 0
    while len(now_flash_coords) > 0:
        n_flashes += len(now_flash_coords)
        for flash_pos in now_flash_coords:
            just_flashed_mask[flash_pos[0], flash_pos[1]] = 1
            flashing_nbr_coords = (NBR_OFFSETS + flash_pos)
            flashing_nbr_coords = flashing_nbr_coords[
                np.logical_and(
                    flashing_nbr_coords.min(axis=1) >= 0,  
                    flashing_nbr_coords.max(axis=1) < grid_shape)
            ].T
            energy_lvls[flashing_nbr_coords[0], flashing_nbr_coords[1]] += 1
        energy_lvls = energy_lvls * np.logical_not(just_flashed_mask)
        now_flash_coords = np.argwhere(energy_lvls > 9)
    return energy_lvls, n_flashes

total_flashes = 0
state = data
step_no = 0
all_flashed_step = -1

while(True):
    state, n_flashed = octo_step(state)
    if step_no < 100:
        total_flashes += n_flashed
    if n_flashed == 100:
        all_flashed_step = step_no + 1
        break
    step_no += 1

print (f"Part 1: {total_flashes} total flashes by step 100")
print (f"Part 2: all octopis flash on step {all_flashed_step}")