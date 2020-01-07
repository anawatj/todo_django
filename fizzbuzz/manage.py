
import sys

def main():
    n = input("prompt")
    if isinstance(n,int):
       fizzbuzz(n)
    elif isinstance(n,float):
        fizzbuzz(n)
    elif n.isdigit():
        fizzbuzz(int(n))
    else:
        print "argument error"


def fizzbuzz(n):
    index = 1
    while index<=n:
        if index % 3 == 0 and index % 5 ==0 :
            print "FizzBuzz"
        elif index % 3 ==0 :
            print "Fizz"
        elif index % 5 ==0 :
            print "Buzz"
        else :
            print str(index)
        index=index+1
main()