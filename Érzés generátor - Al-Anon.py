import random

erzesek = [
    "öröm", "szomorúság", "harag", "félelem", "meghatottság",
    "hála", "csalódottság", "nyugalom", "izgatottság", "kimerültség",
    "remény", "szégyen", "düh", "bűntudat", "büszkeség",
    "kíváncsiság", "unottság", "irigység", "szeretet", "gyűlölet",
    "megkönnyebbülés", "szorongás", "elégedettség", "vágyakozás", "aggodalom",
    "inspiráció", "lelkesedés", "kétség", "megértés", "zavarodottság",
    "bizonytalanság", "empátia", "önbizalom", "kiábrándultság", "figyelmesség",
    "sajnálat", "önutálat", "türelem", "undor", "megvetés",
    "csodálkozás", "elégedetlenség", "meglepetés", "vágy", "bizalom",
    "elutasítás", "elfogadás", "szenvedély", "ragaszkodás", "szépségérzet",
    "tehetetlenség", "megnyugvás", "féltékenység", "kicsinyesség", "sértettség",
    "csodálat", "bizalmatlanság", "gondoskodás", "fájdalom",
    "szétszórtság", "összeszedettség", "vádlás", "felismerés", "hit",
    "elhagyatottság", "összekapcsolódás", "megvilágosodás", "lemondás", "önsajnálat",
    "elragadtatás", "nyomás", "megbánás", "akaraterő", "kitartás",
    "kegyelem", "alázat", "rémület", "döntésképtelenség", "összhang",
    "szabadság", "korlátozottság", "törődés", "határozottság", "béke", "bosszú", "intimitás", "önfeláldozás", "szégeynlősség", "önuralom", "közöny", "szükséglet", "közelség", "sérülékenység", "önelfogadás", "elhivatottság", "önigazolás", "magány", "megtisztulás", "nosztalgia", "sajnálkozás", "képmutatás", "gyengédség", "fegyelem", "kalandvágy", "önzés", "csodavárás", "önostorozás", "önkifejezés", "hősiesség", "lehangoltság", "reménytelenség", "hűség", "jóindulat", "elengedés", "megalázottság", "ártatlanság", "megbecsülés", "túlpörgés", "elidegenedés", "elégtétel"
]


szam = int(input("Válassz egy számot 1 és 120 között!"))

if 1 <= szam <= 120:
     veletlen_erzes = random.choice(erzesek)
     print(f"A(z) {szam}-es számhoz most az alábbi érzést rendeltük: {veletlen_erzes}")
else:
     print("Kérlek, érvényes egész számot adj meg 1 és 120 között.")
     
  
     

   