import random
def high_low():
                print "wanna play high low"
                a=raw_input("press y to begin")
                if a=='y':
                                c=input("which number do you like(1,9){this will decide number of digits in the number}")
                                b=random.randint(10**(c-1),(10**c)-1)
                print "instructions for the game are as follows"
                print "you have to guess a number,rest you will understand"
                if c==1:
                                g=3
                                print "you have",3," chances to guess"
                elif c==2:
                                g=5
                                print "you have",5,"chances to guess"
                elif c>2:
                                g=c*4-2
                                print "you have",(c*4-2),"chances to guess"
                e=0
                print "ok ready"
                while True:
                                d=input("guess the c digit number")
                                if d>b:
                                                e=e+1
                                                print "too high"
                                                
                                elif d<b:
                                                e=e+1
                                                print "too low"
                                if g-e==1:
                                                print "1 try left"
                                else:
                                                print g-e,"tries left"
                                if e==g:
                                                print "you have lost the game"
                                                print "the number is",b
                                                break
                                elif d==b:
                                                print "you won the game"
                                                print "congoooooooooooooooooooooo"
                                                break
high_low()

while True:
                f=raw_input("wanna play again y/n")
                if f=='y':
                                high_low()
                elif f=='n':
                                print "ok bye bye"
                                break
                                
