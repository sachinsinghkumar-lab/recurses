def tail_sum(n, acc=0):
    if n == 0:
        return acc 

    return tail_sum(n-1, acc + n)

input("tail recursion is the last action witht he recursive call with an accumulator. press enter")
print("  tail sum of 4", tail_sum(4),"4+3+2+1")
print(" tail sum o 5", tail_sum(5),"5+4+3+2+1")

n = int(input("enter a number, try 3 or 6:"))
guess = input("what do u think the tail of it is???")
input("tail sum adds n to acc, where acc rises and n goes down. press enter")
print("  tail_sum is(" + str(n) + ")=", tail_sum(n)," ur guess:", guess)
