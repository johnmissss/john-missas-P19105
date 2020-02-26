arkart=int(input("dwse arithmo "))
a=str(arkart)
card=[]
card2=[]
for i in a:
  k=int(i)
  card.append(k)

for i in range (0,15,2):
  pol=card[i]*2
  a=str(pol)
  n=len(a)
  if n>1:
    r1=int(a[0])
    r2=int(a[1])
    sum=r1+r2
    card2.insert(i,sum)
  else:
    card2.insert(i,pol)  
print"o arithmos thw karta einai",card 
k=0  
for i in range(0,15,2):
  card.pop(i)
  card.insert(i,card2[k])
  k=k+1
syn=0  
for i in range(16):
  syn=syn+card[i]
if syn%10==0:
  print "h karta einai egkiri"
else:
  print"den einai egkiri"