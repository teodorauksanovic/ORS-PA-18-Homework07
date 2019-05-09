"""
===================   TASK 4  ====================
* Name: Number of Appearances
*
* Write a function that will return which element
* of integer list has the greatest number of
* appearances in that list.
* In case that multiple elements have the same
* number of appearances return any.
*
* Note: You are not allowed to use built-in
* functions.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

# Write your function here

def brojpojavljivanja(lista):

    t= {}
    duzina = len(lista)
    brojjavljanja = 0

    for i in range(duzina):

        if lista[i] not in t:

            for broj in range(i,duzina):


                if lista[broj] == lista[i]:

                    brojjavljanja += 1

                dati_broj = lista[i]

                t[dati_broj] = brojjavljanja
        brojjavljanja=0

    niz = []

    for key in t:

        niz.append(t[key])
    maximum = niz[0]

    for i in range(len(niz)):
        if niz[i]  >maximum:
            maximum=niz[i]


    for key in t:
        if maximum==t[key]:
            return key



def main():

    lista = [5,3,2,5,3,2,0,2,8,6]
    x = brojpojavljivanja(lista)

    print("Broj sa najvise ponavljanja: " +str(x))
    pass

main()