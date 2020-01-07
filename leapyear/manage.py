import sys

def main():
    n = input("Year:")
    if isinstance(n,int):
        print leap(n)
    elif n.isdigit():
        print leap(int(n))
    else:
        print  "argument is invalid"

def leap(n):
    is_leap = False
    if n%400 == 0 :
        is_leap=True
    elif n%100 ==0 :
        is_leap=False
    elif n%4==0:
        is_leap=True
    else:
        is_leap=False
    return is_leap

main()