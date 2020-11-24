import haravasto

def tulvataytto(kentta, xkoord, ykoord):
    lista = [(xkoord, ykoord)]
    if kentta[ykoord][xkoord] == "x":
        pass
    else:
        for i in lista:
            lista.remove(i)
            kentta[i[1]][i[0]] = "0"
            x1, x2, x3 = i[0], i[0] - 1, i[0] + 1
            y1, y2, y3 = i[1], i[1] - 1, i[1] + 1
            koordinaatit = [
	        (x3, y3), (x3, y2), (x2, y2), (x2, y3), (x1, y2), (x1, y3), (x3, y1), (x2, y1)]
            if kentta[y3][x3] == " ":lista.append((x3, y3))
            if kentta[y2][x3] == " ":lista.append((x3, y2))
            if kentta[y2][x2] == " ":lista.append((x2, y2))
            if kentta[y3][x2] == " ":lista.append((x2, y3))
            if kentta[y2][x1] == " ":lista.append((x1, y2))
            if kentta[y3][x1] == " ":lista.append((x1, y3))
            if kentta[y1][x3] == " ":lista.append((x3, y1))
            if kentta[y1][x2] == " ":lista.append((x2, y1))
            
def main():
	haravasto.lataa_kuvat("spritet")
	haravasto.luo_ikkuna(500, len(planeetta) * 40)
	haravasto.aseta_piirto_kasittelija(piirra_kentta)
	haravasto.aloita()
def piirra_kentta():
	haravasto.tyhjaa_ikkuna()
	haravasto.piirra_tausta()
	#haravasto.piirra_tekstia
	haravasto.aloita_ruutujen_piirto()
	for y, sisalto in enumerate(planeetta):
		for x, sis in enumerate(sisalto):	
				haravasto.lisaa_piirrettava_ruutu(sis, x * 40, y * 40)
	haravasto.piirra_ruudut()


planeetta = [
    [" ", " ", " ", "x", " ", " ", " ", " ", " ", " ", " ", "x", " "], 
    [" ", " ", "x", "x", " ", " ", " ", "x", " ", " ", " ", "x", " "], 
    [" ", "x", "x", " ", " ", " ", " ", "x", " ", " ", "x", "x", " "], 
    ["x", "x", "x", "x", "x", " ", " ", "x", " ", "x", " ", " ", " "], 
    ["x", "x", "x", "x", " ", " ", " ", " ", "x", " ", "x", " ", " "], 
    [" ", " ", "x", " ", " ", " ", " ", " ", " ", "x", " ", " ", " "]
]
print(planeetta)
tulvataytto(planeetta, 1, 1)
print(planeetta)
main()
"""
koordinaatit = [
	(x1, y1), (x3, y3), (x3, y2), (x2, y2), (x2, y3), (x1, y2), (x1, y3), (x3, y1), (x2, y1)]
"""