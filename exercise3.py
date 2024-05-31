#Schreiben Sie eine Funktion namens steigung_funktion(), die die Steigung der durch zwei Punkte verlaufenden Geraden berechnet. Die Funktion nimmt eine Liste mit vier Elementen als Argument. Die ersten beiden Elemente sind die x-y-Koordinaten des ersten Punktes und das dritte und vierte Element der Liste sind die x-y-Koordinaten des zweiten Punktes. Wenn die Veränderung von x gleich Null ist, d. h. die Gerade vertikal verläuft, gibt die Funktion "Die Steigung ist nicht definiert." aus.
def steigung_funktion (liste):
    x1 = liste [0]
    y1 = liste [1]
    x2 = liste [2]
    y2 = liste [3]
    
    delta_x = x2-x1
    delta_y = y2-y1
    
    #steigung = delta_y/delta_x
    
    if delta_x == 0:
        print("Die Steigung ist nicht definiert")
    else:
        steigung = delta_y/delta_x
        print(steigung)
    
    
   # erster Ansatz: if (y2-y1)//(x2-x1) == 0:
    #    print("Die Steigung ist nicht definiert")
    #else 
#Beispiele/Test:
steigung_funktion([8, 3, 8, 4])
steigung_funktion([4, 4, 8, 4])
