B=[[3, 4, 5, 6, 1],
  [1, 3, 4, 7, 8],
  [4, 6, 1, 10, 9],
  [3, 9, 6, 4, 8],
  [2, 7, 4, 9, 10]]
d1=B[0][0]+B[1][1]+B[2][2]+B[3][3]+B[4][4]
d2=B[0][4]+B[1][3]+B[2][2]+B[3][1]+B[4][0]
c1=0
c2=0
c3=0
c4=0
c5=0
for i in B:
    c1+=i[0]
    c2+=i[1]
    c3+=i[2]
    c4+=i[3]
    c5+=i[4]
print("suma primei coloane-", c1)
print("suma coloanei doi-", c2)
print("suma coloanei trei-", c3)
print("suma coloanei patru-", c4)
print("suma coloanei cinci-", c5)
print("suma primului rind-", sum(B[0]))
print("suma rindului doi-", sum(B[1]))
print("suma rindului trei-", sum(B[2]))
print("suma rindului patru-", sum(B[3]))
print("suma rindului cinci-", sum(B[4]))
print("diagonala principala-", d1)
print("diagonala secundara-", d2)
