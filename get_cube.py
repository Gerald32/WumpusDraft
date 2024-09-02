import csv
import os
import requests
import time

# Input
SETS = ["akh", "dom", "war", "stx", "znr"]
CUBE_NAME = "TestCube"
WITH_RARITY = True

def check(r):
    if r.status_code != 200:
        print("request failed")
        exit(1)
    print("request success")

def get_names(r):
    names = []
    csvfile = r.text.split("\n")[1:-1] # trim headers and terminating newline
    lines = csv.reader(csvfile)
    for l in lines:
        if WITH_RARITY:
            names.append([l[6], l[5]])
        else:
            names.append(l[6])
    return names

# build query from SETS
query = "+OR+".join(["set%3A" + s for s in SETS])
# make url base
base = "https://api.scryfall.com/cards/search?order=name&format=csv&q=(" + query + ")&page=1"

result = requests.get(base)
check(result)
cube = []

while result.headers['X-Scryfall-Has-More'] == "true":
    time.sleep(0.1)
    cube += get_names(result)
    new_url = result.headers['X-Scryfall-Next-Page']
    result = requests.get(new_url)
    check(result)

# add last page
cube += get_names(result)

if CUBE_NAME == "":
    print(cube)
else:
    cube_idx = 1
    filename = "C:\\Users\\Gerald\\Downloads\\" + CUBE_NAME + str(cube_idx) + ".txt"
    while os.path.exists(filename):
        cube_idx += 1
        filename = "C:\\Users\\Gerald\\Downloads\\" + CUBE_NAME + str(cube_idx) + ".txt"
    with open(filename, 'w+') as f:
        for card in cube:
            if WITH_RARITY:
                f.write(",".join(card) + "\n")
            else:
                f.write(card + "\n")
    print("Saved to " + filename)
