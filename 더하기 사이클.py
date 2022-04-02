a=int(input())
q=a
count=0
result=0
while(a!=result):
    
    if a==0:
        count=1
        break;
    elif q<10:
        i=0
        j=q
        k=q
        result=10*j+k
    
    elif q>=10:
        i=int(q/10)
        j=int(q%10)
        k=i+j
        if k>=10:
            k=int(k%10)
        result=(j*10)+k
    
    count+=1
    q=result

if a==0:
    count=1
print(count)
