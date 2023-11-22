szovegkiir = f"Hello world"
print(szovegkiir)


nev = input("Hogy hívnak: ")
szovegkiir = f"Hello {nev}!"
print(szovegkiir)



#Változók
alapSzam, ketszeres,szovegKiir = 0,0,""

alapSzam = int(input("Kérem a számot: "))
ketszeres = 2*alapSzam
szovegKiir = f"A szám: {alapSzam} ketszerese: {ketszeres}"
print(szovegKiir)




#Változók
elso, masodik,ossszeg,kulonbseg,szorzat,hanyados,szovegKiir = 0,0,0,0,0,0,""

elso= int(input("Kérem az első számot: "))
masodik= int(input("Kérem  a második számot: "))

osszeg = elso + masodik
kulonbseg = elso - masodik
szorzat = elso * masodik
hanyados = elso / masodik

szovegKiir = f"A számok {elso},{masodik}"
szovegKiir += f"A összege {ossszeg}"
szovegKiir += f"Külömbség {kulonbseg}"
szovegKiir += f"Szorzat {szorzat}"
szovegKiir += f"Hanyados {hanyados:.2f}"

print(szovegKiir)






# Változok
elso,masodik,nagyobb, egyenlo,szovegkiir = 0,0,0,0,""

elso = int(input("Kérem az első számot: "))
masodik = int(input("Kérem a második számot: "))

if elso <= masodik:
    nagyobb = masodik
        
else:
    nagyobb = elso

szovegkiir = f"A nagyobb szám: {nagyobb}"

print(szovegkiir)








#Változók
elso,masodik,harmadik,legkisebb,szovegkiir = 0,0,0,0,""


#Segédváltozók
kisebb = 0



elso = int(input("Kérem az első számot: "))
masodik = int(input("Kérem a második számot: "))
elso = int(input("Kérem a harmadik számot: "))

if elso <= masodik:
    kisebb = elso
else:
    kisebb = masodik
    
if kisebb <= harmadik:
    legkisebb = kisebb
    
else:
    legkisebb = harmadik
        
szovegkiir = f"A legkisebb szám {legkisebb}"

print(szovegkiir)