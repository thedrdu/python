#This is my first python program - High - Low game
#author Jeffrey Du @1/20/2016
print "Welcome to High-Low!"
from random import randint
N = (randint(1,100))

x = input('Guess a number from one to one hundred:')
while x != N:
    if x < N:
        print "Too low!"
    elif x > N:
        print "Too high!"

    x = input('Guess again:')


if x == N:
    print "You got it!"
