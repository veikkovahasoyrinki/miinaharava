import haravasto
def kasittele_hiiri(x, y, nappi, muokkausnappain):	
	if nappi == haravasto.HIIRI_VASEN:
		painettu_nappi = "vasen"
	elif nappi == haravasto.HIIRI_OIKEA:
		painettu_nappi = "oikea"
	else:
		painettu_nappi = "keski"
	print("kusti on homo {} painettiin kohdasssa {}, {}".format(painettu_nappi, x, y))
	
	
	
def main():
	haravasto.luo_ikkuna()
	haravasto.aseta_hiiri_kasittelija(kasittele_hiiri)
	haravasto.aloita()
	
if __name__ == "__main__":
    main()

