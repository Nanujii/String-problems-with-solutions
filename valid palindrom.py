#Valid Palindrome
def AL(P):
    L=""
    for i in P:
        if i.isalnum():
            L=L+i.upper()
        else:
            continue
    L1=L[::-1]
    if L==L1:
        print("True")
    else:
        print("False")

K="race a car"
AL(K)
