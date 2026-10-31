def fib(n):
    if n < 1:
        return n
    return fib(n-1) + fib(n-2)

input("tree recursion = two recursive calls PER stop . press enter")
print("  fib of 5 is:", fib(5))
print("fib of 6 is:", fib(6))

n = int(input("enter a number:"))
guess = input(" what do u think"+str(n)+"fib/tree recurse is??")
input("tree recursion is when it roots oiut")