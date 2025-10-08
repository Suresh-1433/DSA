def compute_factorial(n):
    if n==1:
        return 1
    elif n==0:
        return 1
    return n*compute_factorial(n-1)
    # Complete this recursive function
num = int(input())
res=compute_factorial(num)

print(res)# Call the compute_factorial function
