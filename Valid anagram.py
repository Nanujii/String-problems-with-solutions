def Ana(s,t):
    L=[]
    H=0
    for i in s:
        L.append(i)
    for i in t:
        if i in L:
            continue
        else:
            H=H+1
    if H==0:
        print("True")
    else:
        print("False")

s= "rat"
t = "tar"
Ana(s,t)
    
