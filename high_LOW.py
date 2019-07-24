import random
def randomizer(c):
    m=random.randint(1,100)
    if m%3==0:
        a=random.randint(1,3)
    if m%3==1:
        a=random.randint(4,6)
    if m%3==2:
        a=random.randint(7,9) 
    for i in range(0,c-1):
        b=random.randint(0,9)
        a=a*10+b
    return a

def chances(c):
    n=0
    b=10**c
    a=2
    while 1!=0:
        if (2**n)>b:
            return n-1
        n=n+1
        
def high_low():
                print ("Wanna play high low")
                a=raw_input("Press y to begin")
                if a=='y':
                                c=input("Which number do you like(1,9){this will decide number of digits in the number}")
                                b=randomizer(c)
                print ("Instructions for the game are as follows")
                print ("You have to guess a number,rest you will understand")
                if c==1:
                                g=chances(c)
                                print ("You have",g" chances to guess")
                elif c==2:
                                g=chances(c)
                                print ("You have",g"chances to guess")
                elif c>2:
                                g=chances(c)
                                print ("You have",g"chances to guess")
                e=0
                print "ok ready"
                while True:
                               d=input("guess the c digit number")
                                if d>b:
                                                e=e+1
                                                print ("too high")
                                                
                                elif d<b:
                                                e=e+1
                                                print ("too low")
                                if g-e>1 and d!=b:
                                                print (g-e,"tries left")
                                if g-e==1 and d!=b:
                                                print ("1 try left")
                                if e==g:
                                                print ("you have lost the game")
                                                print ("the number is",b)
                                                break
                                elif g-e!=0 and d==b:
                                                print ("you won the game")
                                                print ("congoooooooooooooooooooooo")
                                                break
high_low()

while True:
                f=raw_input("Wanna play again y/n")
                if f=='y':
                                high_low()
                elif f=='n':
                                print ("Ok bye bye")
                                break
                                
