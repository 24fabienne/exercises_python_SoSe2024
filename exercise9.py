#HA

def buchstabe_ändern(string, buchstabe):
    
    vokale = "aeiou"
    
    def buchstabe_ersetzen(x, y, z):
        
        x_list = list(x.lower())
        
        for i in range (len(x_list)):
            
            if x_list[i] == y:
                
                x_list[i] = z
                
        return "".join(x_list)
        
    for v in vokale:
            print(buchstabe_ersetzen(x=string, y=buchstabe, z=v), end=" ")
            
buchstabe_ändern(string = "banana", buchstabe = "a")



#list("Hi, Berlin!".lower())


#Arrays Übung 1

import numpy as np

#a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

a = np.arange(1,13).reshape(3,2,2)
print(a)

type(a)
#oder in 2 schritten:
    #a=np.arange(1,13)
    #a_3D=a.reshape(3,2,2)
    
    
#Übung 2

a.ndim
a.shape
a.size
a.dtype

#Übung 3

A = np.identity(5, dtype="int")

A[3:, : 2] = 2     #immer zeilen zuerst
print(A)

A[:2, 3:] = 3
print(A)





