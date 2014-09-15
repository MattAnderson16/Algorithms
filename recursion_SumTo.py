def SumTo(n):
    if n == 1:
        result = 1
    else:
        result = n + SumTo(n-1)
    return result

n = int(input("Please enter a positive integer value >> "))
result = SumTo(n)
print(result)
