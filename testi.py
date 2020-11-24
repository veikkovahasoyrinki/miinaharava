"""
import random

tila = {
    "kentta": []
}
kentta = []
for rivi in range(10):
    kentta.append([])
    for sarake in range(15):
        kentta[-1].append(" ")
tila["kentta"] = kentta
tila["kentta"][0][0] = "aasi"
print(len(tila["kentta"][0]), len(tila["kentta"]))
jaljella = []
for x in range(15):
    for y in range(10):
        jaljella.append((x, y))

for i in range(1, 9):
	rand = random.choice(jaljella)
	xkoord, ykoord = rand[0], rand[1]
	tila["kentta"][ykoord][xkoord] = "x"
#print(tila["kentta"])
"""
kdapjsd = [(1, 0)]
print(kdapjsd[0][1])