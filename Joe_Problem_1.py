"""
If we list all the natural numbers below 10 that are multiples of
3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

myList = set()
N5      = 1000//5
N3      = 1000//3+1

for i in range(1,N3):
    myList.add(3*i)
    if i<N5:
        myList.add(5*i)
        
print(sum(myList))

    