#Author: Jeffrey Du
#Last Modified 1/17/2016
#This is a lottery simulator game.
#Chances of winning are slim, and may take hours, if not days.
print "Welcome to the lottery!"
from random import randint
N = (randint(1000,9999))
print N
x = input('Choose a 4 digit lottery number:')
while x != N:
    if x != N:
        print "Sorry, your ticket is not a winner!"
        x = input('Try another 4 digit lottery number:')


if x == N:
    from random import randint
    P = (randint(10000000,500000000))
    print "Congratulations! You have won " + str(P) + " dollars!"
