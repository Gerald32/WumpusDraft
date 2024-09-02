import os
import random

# Input
CUBE_FILE = "C:\\Users\\Gerald\\Downloads\\TestCube4.txt"
POOL_NAME = "Colin"
NUM_PACKS = 18
NUM_R = 1
NUM_U = 3
NUM_C = 10

r = []
u = []
c = []

with open(CUBE_FILE) as f:
    for l in f.readlines():
        line = l[:-1].split(",")
        name = line[0]
        rarity = line[1]

        match rarity:
            case "R" | "M":
                r.append(name)
            case "U":
                u.append(name)
            case "C":
                c.append(name)

# pick NUM_R * NUM_PACKS from r and so on
cards = []

cards += random.choices(r, k=NUM_R * NUM_PACKS)
cards += random.choices(u, k=NUM_U * NUM_PACKS)
cards += random.choices(c, k=NUM_C * NUM_PACKS)


if POOL_NAME == "":
    for c in cards:
        print(c)
else:
    idx = 1
    filename = "C:\\Users\\Gerald\\Downloads\\" + POOL_NAME + str(idx) + ".csv"
    while os.path.exists(filename):
        idx += 1
        filename = "C:\\Users\\Gerald\\Downloads\\" + POOL_NAME + str(idx) + ".csv"
    with open(filename, 'w+') as f:
        f.write("name\n")
        for c in cards:
            f.write(c + "\n")
    print("Saved to " + filename)


