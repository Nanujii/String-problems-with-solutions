pat="aaaa"
st="dog cat cat dog"
L=st.split()
L1=[]
D={}
for i in range(len(pat)):
    if i not in D:
        D.update({pat[i]:L[i]})
for i in range(len(pat)):
    L1.append(D.get(pat[i]))
if L==L1:
    print("True")
else:
    print("False")
