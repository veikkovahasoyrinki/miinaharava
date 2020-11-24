import haravasto
import random

tila = {
    "kentta": []
}

def miinoita(kentta, ruudut, miinat):
	#x, y =len(tila["kentta"][0]), len(tila["kentta"])
	#koko = x * y
	numerot = []
	for i in range(0, miinat):
		rand = random.choice(ruudut)
		ruudut.remove(rand)
		xkoord, ykoord = rand[0], rand[1]
		kentta[ykoord][xkoord] = "x"

def piirra_kentta():
	haravasto.tyhjaa_ikkuna()
	haravasto.piirra_tausta()
	#haravasto.piirra_tekstia
	haravasto.aloita_ruutujen_piirto()
	for y, sisalto in enumerate(tila["kentta"]):
		for x, sis in enumerate(sisalto):	
				haravasto.lisaa_piirrettava_ruutu(sis, x * 40, y * 40)
	haravasto.piirra_ruudut()
	
def main():
	haravasto.lataa_kuvat("spritet")
	haravasto.luo_ikkuna(600, 400)
	haravasto.aseta_piirto_kasittelija(piirra_kentta)
	haravasto.aloita()


kentta = []
for rivi in range(10):
	kentta.append([])
	for sarake in range(10):
		kentta[-1].append(" ")
tila["kentta"] = kentta
"""jaljella = []
for x in range(10):
	for y in range(10):
		jaljella.append((x, y))
miinoita(tila["kentta"], jaljella, 10)
"""
main()
