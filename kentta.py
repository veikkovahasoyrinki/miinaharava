def piirra_kentta():
	haravasto.tyhjaa_ikkuna()
	haravasto.piirra_tausta()
	#haravasto.piirra_tekstia
	haravasto.aloita_ruutujen_piirto()
	for y, sisalto in enumerate(tila["kentta"]):
		for x, sis in enumerate(sisalto):	
				haravasto.lisaa_piirrettava_ruutu(sis, x * 40, y * 40)
	haravasto.piirra_ruudut()