numToGen = 10

import random

f = open("names.txt", "r")
outF = open("classRoll.txt", "w")

i = 0
while i < numToGen:
    curName = f.readline()
    curName = curName.strip()
    dub = random.randint(1, 5)
    for x in range(dub):
        grade = random.randint(0, 99)
        # print(curName + "\t\t\t\t" + str(grade), file=outF)
        print(f"{curName:20s}{grade:02d}", file=outF)
    i = i + 1

f.close()
outF.close()

toShuff = open("classRoll.txt").readlines()
random.shuffle(toShuff)
open("classRoll.txt", "w").writelines(toShuff)

