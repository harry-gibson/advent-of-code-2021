import numpy as np

crab_positions = np.genfromtxt('./input.txt', delimiter=',', dtype=int)

# PART 1
least_fuel = np.inf
least_fuel_pos = np.inf
for i in np.arange(crab_positions.max()):
    fuel_per_sub = np.abs(crab_positions - i)
    fuel = fuel_per_sub.sum()
    if fuel < least_fuel: 
        least_fuel = fuel
        least_fuel_pos = i

print(f"Part 1: {least_fuel}")


# PART 2
least_fuel = np.inf
least_fuel_pos = np.inf
triangular_number = lambda n: n * (n + 1) // 2
for i in np.arange(crab_positions.max()):
    fuel_per_sub = triangular_number(np.abs(crab_positions-i))
    fuel = sum(fuel_per_sub)
    if fuel < least_fuel: 
        least_fuel = fuel
        least_fuel_pos = i

print(f"Part 2: {least_fuel}")