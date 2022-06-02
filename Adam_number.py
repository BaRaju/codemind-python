n=int(input())
sq=n*n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
sq_rev=rev*rev
rev_sq_rev=0
while sq_rev>0:
    r=sq_rev%10
    rev_sq_rev=rev_sq_rev*10+r
    sq_rev=sq_rev//10
if sq==rev_sq_rev:
    print('True')
else:
    print('False')