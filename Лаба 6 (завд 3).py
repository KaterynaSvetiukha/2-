def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

x = set(range(8, 23))
y = {n for n in x if prime(n)}

print("Множина x:", x)
print("Множина y:", y)
    