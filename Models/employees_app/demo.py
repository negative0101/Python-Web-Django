# U(0)=0, U(1)=1 и U(n) = p*U(n-1) - q*U(n-2)

# def recursion_Lucas(p,q,n):
#     p,q = 1,2
#     if n == 0:
#         return 2
#     elif n == 1:
#         return 1
#     return recursion_Lucas(p * (n - 1)) - recursion_Lucas(q * (n - 2))
#
# print(recursion_Lucas(5,5,6))


def lucas(n,p,q):
    def wrapper(p,q):
        return p*(n-1) - q*(n-2)

    if n==0:
        return 2
    if n==1:
        return 1
    return lucas(n-1) + lucas(n-2)


print(lucas(3))
