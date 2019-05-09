
"""
===================   TASK 2  ====================
* Name: Recursive Sum
*
* Write a recursive function that will sum given
* list of integer numbers.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

# Write your function here


def sum(n):
    if not n :
        return 0
    return n[0] + sum(n[1:])

def main():
    list = [1,2,3,4,5]
    ssum = sum(list)
    print("The sum is: ", ssum)
    pass

main()
