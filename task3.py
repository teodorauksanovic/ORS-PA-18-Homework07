"""
===================   TASK 3  ====================
* Name: Insertion Sort
*
* Write a function that will implement insertion sort
* algorithm. Generate list of 1000 random integer
* numbers and sort the list using your function.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

# Write your function here


import random
def funkcija(listn):
    a = []
    while len(listn) >= 1:
        minimum = listn[0]
        for el in listn:
            if el < minimum:
                minimum = el


        a.append(minimum)
        listn.remove(minimum)

    return a


def main():
    listn = []
    for i in range(0,1000):
        listn.append(random.randint(0,1000))
    rd = funkcija(listn)
    print(rd)
    pass

main()