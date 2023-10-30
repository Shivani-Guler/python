# def counter(start,stop):
#     if start==stop:
#         print("counting",start)
#         return
#     counter(start+1,stop)
#     print("counting",start)
# counter(10,30)

#---------------------------------------

# def counter(start,stop):
#     if start==stop:
#         return
#     print("counting",start)
#     counter(start+1,stop)
# counter(10,30)

#------------------factorial-------------------

# def fact(n):
#     if n:
#         return n*fact(n-1)
#     return 1
# print(fact(4))

#---------------fibbonaci----------------------

def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(5)) 