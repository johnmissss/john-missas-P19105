fin = open('exerc2', 'w')
fin.write("wrrrrrraia thleorasi ayth \n")
fin.write("ekkkkkw miden eyrw \n")
fin.write("ccccccinepws den tha tin agoraswwww \n")
fin.write("ektos an einaii ffffffthini")
fin.close() 
fin=open("exerc2","r")
r=fin.read()
fin.close()
f="aeiuoyAEIUOY"
s="!,.,;"
w=""
for i in r:
  if i not in f and i not in s and i !="\n":
    w=w+i
print w   
sym="fckr"
plsym=0
plithos=0
a=0
w2=w+" "
for i in w2:
  if i !=" ":
    if i in sym:
      plsym=plsym+1  
    else:
      plithos=plithos+1
  else:
    a=a+1
    if plsym>plithos:
      print"h lexi stin thesi",a
      print"einai kakh"
    else:
      print"h lexi stin thesi",a
      print"einai kalh" 
    plsym=0
    plithos=0
