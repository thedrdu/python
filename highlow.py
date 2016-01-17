#Author: Jeffrey Du
#Last Modified 1/17/2016
#This is my first python program: A High - Low game

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
