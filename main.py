import haravasto
from pyglet.window import key
import kentankysyja
import random
tila = {
    "kentta": [

    ]
}
jaljella = []

def piirra_kentta():
    haravasto.tyhjaa_ikkuna()
    haravasto.piirra_tausta()
    #haravasto.piirra_tekstia
    haravasto.aloita_ruutujen_piirto()
    for y, sisalto in enumerate(tila["kentta"]):
        for x, sis in enumerate(sisalto):
                if sis == "x":sis = " "
                haravasto.lisaa_piirrettava_ruutu(sis, x * 40, y * 40)
    haravasto.piirra_ruudut()

def paivita_kentta():
    #haravasto.tyhjaa_ikkuna()
    #haravasto.piirra_tausta()
    haravasto.aloita_ruutujen_piirto()
    if tila["kentta"][kasittele_hiiri.ykoord][kasittele_hiiri.xkoord] == " ":tila["kentta"][kasittele_hiiri.ykoord][kasittele_hiiri.xkoord] = "0"
    haravasto.lisaa_piirrettava_ruutu(tila["kentta"][kasittele_hiiri.ykoord][kasittele_hiiri.xkoord], kasittele_hiiri.xkoord * 40, kasittele_hiiri.ykoord * 40)
    #y, sisalto = enumerate(tila["kentta"])
    #x, sis = enumerate(sisalto)
    #haravasto.lisaa_piirrettava_ruutu(sis,x * 40, y * 40)
    #for y, sisalto in enumerate(tila["kentta"]):
    #    for x, sis in enumerate(sisalto):
    #            #if sis == " ":sis = "0"
    #            haravasto.lisaa_piirrettava_ruutu(sis, x * 40, y * 40)
    haravasto.piirra_ruudut()
    if tila["kentta"][kasittele_hiiri.ykoord][kasittele_hiiri.xkoord] == "x":haravasto.piirra_tekstia("Hävisit!", 0, 0)


def main2():
    haravasto.aseta_piirto_kasittelija(paivita_kentta)


def miinoita(kentta, ruudut, miinat):
    #x, y =len(tila["kentta"][0]), len(tila["kentta"])
    #koko = x * y
    numerot = []
    for i in range(0, miinat):
        rand = random.choice(ruudut)
        ruudut.remove(rand)
        xkoord, ykoord = rand[0], rand[1]
        kentta[ykoord][xkoord] = "x"

def kasittele_hiiri(x, y, nappi, muokkausnappain):	
    if nappi == haravasto.HIIRI_VASEN:
        painettu_nappi = "vasen"
    elif nappi == haravasto.HIIRI_OIKEA:
        painettu_nappi = "vasen"
    else:
        painettu_nappi = "vasen"
    kasittele_hiiri.xkoord = int(x / 40)
    kasittele_hiiri.ykoord = int(y / 40)
    #if tila["kentta"][ykoord][xkoord] == " ":tila["kentta"][ykoord][xkoord] = "0"
    #if tila["kentta"][ykoord][xkoord] == "x":tila["kentta"][ykoord][xkoord] = "x"
    #if tila["kentta"][ykoord][xkoord] == " "
    main2()
    #print("Hiiren nappia {} painettiin ruudussa {}, {}".format(painettu_nappi, int(x / 40) + 1, int(y / 40) +1 ))

def kasittele_nappain(nappain, muokkausnappain):
        if nappain == key.ESCAPE:haravasto.lopeta()
        if nappain == key.ENTER:
            kentankysyja.kysyja()
            piirtaja()
            main()
def main():
    haravasto.tyhjaa_ikkuna()
    haravasto.lataa_kuvat("spritet")
    haravasto.muuta_ikkunan_koko(kentankysyja.xy[0] * 40, kentankysyja.xy[1] * 40)
    haravasto.aseta_piirto_kasittelija(piirra_kentta)
    haravasto.aseta_hiiri_kasittelija(kasittele_hiiri)
    haravasto.aloita()

def alkupiirto():
    haravasto.piirra_tausta()
    haravasto.piirra_tekstia("Paina enter aloittaaksesi uuden pelin", 0, 400, (0, 0, 0, 255), "serif", 21)
    haravasto.piirra_tekstia("Paina esc lopettaaksesi", 0, 300, (0, 0, 0, 255), "serif", 21)

def alkuvalikko():
    haravasto.luo_ikkuna(500, 500)
    haravasto.aseta_piirto_kasittelija(alkupiirto)
    haravasto.aseta_nappain_kasittelija(kasittele_nappain)
    haravasto.aloita()


def piirtaja():
    kentta = []
    for rivi in range(kentankysyja.xy[0]):
	    kentta.append([])
	    for sarake in range(kentankysyja.xy[1]):
		    kentta[-1].append(" ")
    tila["kentta"] = kentta
    for x in range(kentankysyja.xy[0]):
        for y in range(kentankysyja.xy[1]):
            jaljella.append((x, y))
    miinoita(tila["kentta"], jaljella, int(kentankysyja.xy[0] * kentankysyja.xy[1] / 10))

alkuvalikko()
