for i in range (0,5):
  k=5-i
  for j in range(k):
      print(1,end=" ")
  for j in range(i):
    print(0,end=" ")
  print()

print()

for i in range (1,6):
  k=5-i
  for j in range(k):
      print(0,end=" ")
  for j in range(i):
    print(1,end=" ")
  print()

print()

for i in range (5,0,-1):
  for j in range(1,6,1):
    if i==j:
      print(1,end=" ")
    else:
      print(0,end=" ")
  print()

print()

for i in range (0,5):
  for j in range(0,5):
    if i==j:
      print(1,end=" ")
    else:
      print(0,end=" ")
  print()
print()

for i in range (0,5):
  k=5-i
  for j in range(k):
      print("*",end=" ")
  print()

print()

for i in range (0,6):
  for j in range(i):
      print("*",end=" ")
  print()

print()

for i in range (1,6):
  k=5-i
  for j in range(k):
      print("",end=" ")
  for j in range(i):
    print("*",end=" ")
  print()

print()

for i in range (5):
  for j in range(5):
    print("*",end=" ")
  print()

print()

k=8 # 2*5-2
for i in range (0,5):
  for j in range(0,k):
      print("",end=" ")
  k-=1
  for j in range(0,i+1):
    print("*",end=" ")
  print()
k=3  #5-2
for i in range (5,-1,-1):
  for j in range(k,0,-1):
      print(end=" ")
  k+=1
  for j in range(0,i+1):
    print("*",end=" ")
  print()
