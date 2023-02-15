from Minumoodul import *
try:
    nimed=["a",]
    keskmised_hinnad=[5,]
    nimed, keskmine_hinnad=lapsed(nimed, keskmised_hinnad)
except:
   print("viga")

try:
    while True:
        print(nimed)
        print(keskmised_hinnad)
        menu=int(input("1-print sorteerida kõik nimed A-st Z-ni \n 2-otsin ületäitjat \n 3-otsin keskmine \n 4-otsib keskmist hinde kui nime \n 5 - otsides indeksina keskmist tulemust \n letter - break "))
        if menu == 1:
            nimed, keskmine_hinnad=nimisorter(nimed, keskmised_hinnad)
        elif menu==2:
            best(nimed, keskmised_hinnad)
        elif menu == 3:
            keskmine(nimed, keskmised_hinnad)
        elif menu ==4:
            näe_keskmine_hind(nimed,keskmised_hinnad)
        elif menu ==5:
            minu_funktsionid(nimed,keskmised_hinnad) 
except:
   print("viga")