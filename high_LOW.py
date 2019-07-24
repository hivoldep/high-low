import random
def high_low():
                print "Wanna play high low"
                a=raw_input("Press y to begin")
                if a=='y':
                                c=input("Which number do you like(1,9){this will decide number of digits in the number}")
                                b=random.randint(10**(c-1),(10**c)-1)
                print "Instructions for the game are as follows"
                print "You have to guess a number,rest you will understand"
                if c==1:
                                g=3
                                print "You have",3," chances to guess"
                elif c==2:
                                g=5
                                print "You have",5,"chances to guess"
                elif c>2:
                                g=c*4-2
                                print "You have",(c*4-2),"chances to guess"
                e=0
                print "ok ready"
                while True:
                                d=input("Guess the c digit number")
                                if d>b:
                                                e=e+1
                                                print "Too high"
                                                
                                elif d<b:
                                                e=e+1
                                                print "Too low"
                                if g-e==1:
                                                print "1 try left"
                                else:
                                                print g-e,"Tries left"
                                if e==g:
                                                print "You have lost the game"
                                                print "The number is",b
                                                break
                                elif d==b:
                                                print "You won the game"
                                                print "Congoooooooooooooooooooooo"
                                                break
high_low()

while True:
                f=raw_input("wanna play again y/n")
                if f=='y':
                                high_low()
                elif f=='n':
                                print "ok bye bye"
                                break
                                
