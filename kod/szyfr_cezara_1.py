alfabet = "abcdefghijklmnopqrstuvwxyz"
ilosc_liter = len(alfabet)

def otworz_plik(nazwa_pliku):
    plik = open(nazwa_pliku, 'r')
    ret = plik.read()
    plik.close()
    return ret

def zapisz_plik(nazwa_pliku, dane):
    plik = open(nazwa_pliku, 'w')
    plik.write(dane)
    plik.close()

def szyfruj_tekst(dane, klucz):
    ret = ""
    for i in range(len(dane)):
        litera = dane[i]
        if litera in alfabet:
            index = alfabet.find(litera)
            ret += alfabet[(index + klucz) % ilosc_liter]
        else:
            ret += litera
    return ret

def szyfruj(nazwa_pliku, klucz, mod = "s"):
    tekst = otworz_plik(nazwa_pliku)
    if mod == "d":
        klucz = ilosc_liter - klucz
    zaszyfrowany = szyfruj_tekst(tekst, klucz)
    zapisz_plik(nazwa_pliku, zaszyfrowany)

