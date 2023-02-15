from random import*

def lapsed(n:list,k:list):
    """Täitke nimekirjad vajaliku arvu inimestega. 
    ::param: List n: nimed järajandid
    ::param: List k: keskmised_hinnad järjendid
    :rtype: list, list
    """
    kui=int(input("kui plaju lapsed te tahate näe"))
    for x in range (kui):
        nimi=input("print lapse nimi")
        hind=uniform(1.5, 5)
        hind=round(hind,1)
        n.append(nimi)
        k.append(hind)
    return n,k


def nimisorter(n:list,k:list):       
    """sorteerida kõik nimed A-st Z-ni
    ::param: List n: nimed järajandid
    ::param: List k: keskmised_hinnad järjendid
    :rtype: list, list  
    """
    
    l=len(n)
    for j in range(0,l-1):
        for jj in range(j+1,l):
            if n[j]>n[jj]:
                abi =n[j]
                n[j]=n[jj]
                n[jj]=abi
                abi =k[j]
                k[j]=k[jj]
                k[jj]=abi
    for jjj in range (l):
        print (f"{n[jjj]}, {k[jjj]}")
    return n,k



def best(n:list,k:list):       
    """otsin ületäitjat
    ::param: List n: nimed järajandid
    ::param: List k: keskmised_hinnad järjendid
    :rtype: 
    """
    r=len(n)
    suurepärane = []
    for jj in range (r):
        if k[jj] == 5:
            suurepärane.append(n[jj])
    rr= len(suurepärane)
    if rr <1 :
        print ("ei ole suurepärane")
    else:
        print(f"suurepärane on {suurepärane}")

def keskmine(n:list,k:list):
    """otsib keskmist hinne
    ::param: List n: nimed järajandid
    ::param: List k: keskmised_hinnad järjendid
    :rtype: 
    """
    jj=sum(k)
    jj = jj / len(k)
    jj= round(jj,1)
    print(f"{jj} on keskmine hind")

def näe_keskmine_hind(n:list,k:list):
    """otsib keskmist hinde kui nime
    ::param: List n: nimed järajandid
    ::param: List k: keskmised_hinnad järjendid
    :rtype: 
    """
    doplist = []
    doplist2 = []
    nimi = input("choose nimi from list")
    r=len(n)
    for jj in range (r):
        if nimi == n[jj]:
            doplist.append( n[jj])
            doplist2.append(k[jj])
    rr = len(doplist)
    if rr >1 :
        print(doplist)
        print(doplist2)
        doppose=int(input(f"valige, millise {nimi} soovite valida"))
        doppose = doppose-1
        print(f"{doplist[doppose]} keskmine hind on {doplist2[doppose]}")
    elif rr ==1 :
        print (f"{doplist[0]} keskmine hind on {doplist2[0]}")
    else :
        print("viga")


def minu_funktsionid(n:list,k:list):
    """näitab positsiooni keskmist punktisummat
    ::param: List n: nimed järajandid
    ::param: List k: keskmised_hinnad järjendid
    :rtype: 
    """
    print(n)
    position = int(input("valige isiku positsioon nimekirjast "))
    position = position -1 
    print(f"{n[position]} keskmine hind on {k[position]}")


   
