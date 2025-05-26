import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

t = int(input())
while t:
  n = int(input())
  s = []
  for i in range(1, 27):
    s.append(chr(i+96))
  if n <= 28:
    print("aa"+s[n-3])
  elif n > 28 and n <=53:
    print("a" + s[n-28] + "z")
  else:
    print(s[n-53]+"zz")
  print(s)
  t-= 1
