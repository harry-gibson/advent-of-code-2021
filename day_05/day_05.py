import numpy as np

class pt:
    
    def __init__(self, coord_str):
        x_str, y_str = coord_str.split(',')
        self.x = int(x_str)
        self.y = int(y_str)
    
    def is_orthogonal_to(self, other_pt):
        return self.x == other_pt.x or self.y == other_pt.y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    
class VentLine:
    
    def __init__(self, file_line):
        from_str, to_str = file_line.strip().split(' -> ')
        self.from_pt = pt(from_str)
        self.to_pt = pt(to_str)
    
    def __str__(self):
        return f"{str(self.from_pt)} -> {str(self.to_pt)}"
    
    def is_orthogonal(self) -> bool:
        return self.from_pt.is_orthogonal_to(self.to_pt)
    
    def is_horizontal(self) -> bool:
        return self.from_pt.y == self.to_pt.y
    
    def min_coords(self):
        return (min(self.from_pt.x, self.to_pt.x), min(self.from_pt.y, self.to_pt.y))
    
    def max_coords(self):
        return (max(self.from_pt.x, self.to_pt.x), max(self.from_pt.y, self.to_pt.y))
    
    def draw_line_on_seabed(self, seabed_array):
        if not self.is_orthogonal():
            # could adapt this part2 solution to do part1 as well, just change the arange step
            dx = np.sign(self.to_pt.x - self.from_pt.x)
            dy = np.sign(self.to_pt.y - self.from_pt.y)
            xcoords = np.arange(self.from_pt.x, self.to_pt.x + dx, dx)
            ycoords = np.arange(self.from_pt.y, self.to_pt.y + dy, dy)
            # NB we can't return the index-based slice and update it in the caller as that would 
            # be a copy not a view so the array would not be affected
            seabed_array[ycoords, xcoords] += 1
        
        elif self.is_horizontal():
            # we could return the slice and do the increment it in caller as it's a view
            seabed_array[self.from_pt.y, 
                        self.min_coords()[0]: self.max_coords()[0]+1] += 1

        else:
            # we could return this slice and do the increment in the caller as it's a view
            seabed_array[self.min_coords()[1] : self.max_coords()[1]+1, 
                        self.from_pt.x] += 1
        
vent_lines = [VentLine(line) for line in open('./input.txt').readlines()]
seabed_size_x = max([v.max_coords()[0] + 1 for v in vent_lines])
seabed_size_y = max([v.max_coords()[1] + 1 for v in vent_lines])

# PART 1
orthog_lines = [v for v in vent_lines if v.is_orthogonal()]
board = np.zeros(shape=(seabed_size_y, seabed_size_x), dtype=np.int32)
for ventline in orthog_lines:
    ventline.draw_line_on_seabed(board)
print(f"Part 1: {np.sum(board>1)}")

# PART 2
board = np.zeros(shape=(seabed_size_y, seabed_size_x), dtype=np.int32)
for ventline in vent_lines:
    ventline.draw_line_on_seabed(board)
print(f"Part 2: {np.sum(board>1)}")
