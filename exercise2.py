#def teilbar (x, y): 
 #   if x // y %== 0:
 #      print("x ist durch y teilbar")
 #   elif x // y %!= 0:
 #      print ("x ist  nicht durch y teilbar")
#    else:
  #    if y == 0:
  #     print("Es ist nicht möglich, durch 0 zu teilen!")
  #    elif x == y:
  #      print ("x und y sind gleich")

# Aufgabe: Schreiben Sie eine Funktion, die zwei Argumente x und y annimmt und schreibt "x ist durch y teilbar", wenn x durch y teilbar ist, ansonsten schreibt "x ist nicht durch y teilbar".
# Darüber hinaus schreibt die Funktion "Es ist nicht möglich durch 0 zu teilen!", wenn y gleich Null ist und "x und y sind gleich", wenn x und y gleich sind.
# Bearbeiten Sie die Übung mit spyder. Speichern Sie die Datei als exercise2.py.
#Variante mit Verschachtelung:
def teilbar (x, y):
    if y == 0:
        print("Es ist nicht möglich, durch 0 zu teilen!")
    elif x == y:
        print("x und y sind gleich")
    else:
        if x%y == 0:
            print("x ist durch y teilbar")
        else:
            print("x ist nicht durch y teilbar")

# Reihenfolge der Bedingungen ist essentiell, da Zusatzbedingungen x gleich y und y gleich null. Test:
teilbar(10,4)

#Variante ohne Verschachtelung: s.u.
# Prozentzeichen ist Modulus, drückt Rest der Division der beiden Zahlen aus.
def teilbar(x, y):
    if y == 0:
        print("Es ist nicht möglich, durch 0 zu teilen!")
    elif x == y:
        print("x und y sind gleich")
    elif x%y == 0:
        print("x ist durch y teilbar")
    else:
        print("x ist nicht durch y teilbar")