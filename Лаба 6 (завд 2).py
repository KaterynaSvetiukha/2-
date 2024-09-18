def dublicate():
    A = list(map(int,input("Введіть список: ").split()))
    print(A)

    B = []

    for i in range(len(A)):
        if A.count(A[i]) > 1 and A[i] not in B:
            B.append(A[i])

    print("Список елементів, що повторюються:", B)
    return 

dublicate()