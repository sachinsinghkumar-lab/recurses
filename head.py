def mirror(n):
    if n == 0:
        return 0
    rest = mirror(n-1)
    return rest + 2*n

input("head recursion is recurses first and then adds 2*n on the wya back. press enter")
print("mirror(3)", mirror(3))
print("mirror(4)", mirror(4))

n = int(input("enter ur number."))
guess = input("what is a mirror" + str(n) + "will be")
input("mirror n = mirror(n-1)+2n adds 2n as it unwinds back up")
print(" mirror(" + str(n) + ")=", mirror(n),"  ur guess:", guess)

if guess == n:
    print("wow u did it nicejob")

    