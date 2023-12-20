A="paper"
B="title"
d={}
for i in range(len(A)):
    d.update({A[i]:B[i]})

K=""
for i in A:
    K=K+d.get(i)
if K==B:
    print("TRue",K)
else:
    print("False",K)
    
