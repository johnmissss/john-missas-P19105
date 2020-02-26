import os
fin=open("emmm.txt","r")
text=fin.read()
fin.close()
text=os.linesep.join([s.strip() for s in text.splitlines() if s])
text=" ".join([s.strip() for s in text.split(" ") if s]) 
words=text.split()
w=[(len(wrd),wrd) for wrd in words]
w.sort(reverse=True)
a=w[0]
b=w[1]
c=w[2]
d=w[3]
e=w[4]
A= (a[1])
B= (b[1])
C= (c[1])
D= (d[1])
E= (e[1])
A=A[::-1]
B=B[::-1]
C=C[::-1]
D=D[::-1]
E=E[::-1]
Vowels= ('a', 'e', 'i', 'o', 'u','A','E','I','O','U')
for x in A:
  if x in Vowels:
    A = A.replace(x, '')
print (A)
for x in B:
  if x in Vowels:
    B=B.replace(x,'')
print (B)
for x in Vowels:
  C=C.replace(x,'')
print (C)
for x in Vowels:
  D=D.replace(x,'')
print(D)
for x in Vowels:
  E=E.replace(x,'')
print(E)