#exercise8

#Schreiben Sie eine Funktion vokon_zählen(), die die Anzahl der Vokale und der Konsonanten in einer String zählt (keine Sonderzeichen oder Leerzeichen). Sie können die Methoden lower() und isalpha() verwenden. Die Funktion drückt eine Strings aus, wie unten gezeigt. Nutzen Sie hier eine f-String
#meine lösung (funktioniert, nur ohne Satz):
#def vokon_zählen(wort):
#    vokale = ("aeiou")
#    konsonanten = ("bcdfghjklmnpqrstvwxyz")
#    wort_lower = wort.lower()
#    wort_list = list(wort_lower)
#    wort_vokale = [vokal for vokal in wort_list if vokal in vokale]
#    wort_konsonanten = [konsonant for konsonant in wort_list if konsonant in konsonanten]
#    print(len(wort_vokale))
#    print(len(wort_konsonanten))
    
#vokon_zählen("HI,&%/ BerliN!!")

#vorgegebene lösung + zusatz wort:
    
def vokon_zählen(wort):
    vokale = "aeiou"
    wort_lower = wort.lower()
    
    bn = [i for i in wort_lower if i.isalpha()]
    vn = [k for k in wort_lower if k in vokale]
    
    print(f""""Es gibt im Wort "{wort}" {len(vn)} Vokale und {len(bn) - len(vn)} Konsonanten.""")
          
vokon_zählen("Berlin") #Anführungsstriche nicht vergessen

