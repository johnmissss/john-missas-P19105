def synar (word):
  a=" "
  for i in word:
    k=ord(i)
    g=str(k)
    a=a+g
  n=int(a)  
  return (n)
def ypol(ar):
    if ar<=1:
        return "oxi prwtos"
    w = 2
    while w*w <= ar:
        if ar%w == 0:
            return "oxi prwtos"
        w = w+1
    return "einai prwtos"  
lexi=raw_input("dwse lexi ")
s=synar(lexi)
r=ypol(s)
print r