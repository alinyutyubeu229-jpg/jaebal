
l=list(map(int,input().split()))
    
big=max(l)
total=l[0]+l[1]+l[2]
#if(big<=total-big):
while big >= (total - big):
        big-=1
        total-=1

print(total)

print("pr 성공"")

    
