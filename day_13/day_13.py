import numpy as np

Xs = [] 
Ys = []
folds = []
with open('./input.txt') as file:
    while (line:=file.readline().strip()) != "":
        x, y = line.split(',')
        Xs.append(int(x))
        Ys.append(int(y))
    while (line:=file.readline().strip()) != "":
        instr = line.strip('fold along ')
        axis, pos = instr.split('=')
        folds.append((axis, int(pos)))

xshape = max(Xs) + 1
yshape = max(Ys) + 1
paper = np.zeros(shape=(yshape, xshape), dtype=int)
paper[Ys, Xs] = 1

folded = paper.copy()
for i, instr in enumerate(folds):
    axis, foldline = instr
    if axis=='x':
        assert folded.shape[1] == foldline * 2 + 1
        folded = folded[:, :foldline] + folded[:, foldline+1:][:, ::-1]
    else:
        assert axis=='y'
        assert folded.shape[0] == foldline * 2 + 1
        folded = folded[:foldline, :] + folded[foldline+1:, :][::-1, :]
    if i == 0:
        print(f"Part 1: {(folded>0).sum()}")
print(folds)        

dots = (folded > 0).astype(int)
from matplotlib import pyplot as plt
plt.imshow(dots)
plt.show()
#print(pytesseract.image_to_string(dots.astype(np.int8)))