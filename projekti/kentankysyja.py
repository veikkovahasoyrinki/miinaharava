import ikkunasto
xy = []
def ikkunasto_napin_kasittelija():
    sisaltox = ikkunasto.lue_kentan_sisalto(kysyja.kenttax)
    sisaltoy = ikkunasto.lue_kentan_sisalto(kysyja.kenttay)
    try:
        xy.append(int(sisaltox))
        xy.append(int(sisaltoy))
        ikkunasto.lopeta()
    except ValueError:
        ikkunasto.avaa_viesti_ikkuna("Virhe!", "positiivisia kokonaislukuja, kiitos.", True)
    
def kysyja():
    ikkuna = ikkunasto.luo_ikkuna("Koko")
    kehys = ikkunasto.luo_kehys(ikkuna)
    laatikko = ikkunasto.luo_tekstilaatikko(kehys)
    teksti = ikkunasto.kirjoita_tekstilaatikkoon(laatikko, "Syötä kentän koko (x ruutua kertaa y ruutua)\nYlempään x ja alempaan y")
    kysyja.kenttax = ikkunasto.luo_tekstikentta(kehys)
    kysyja.kenttay = ikkunasto.luo_tekstikentta(kehys)
    nappi = ikkunasto.luo_nappi(kehys, "Paina tästä aloittaaksesi", ikkunasto_napin_kasittelija)
    ikkunasto.kaynnista()