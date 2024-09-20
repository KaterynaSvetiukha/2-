def add_paired():
    A = list(map(int,input("Введіть список: ").split()))
    print(A)

    B = []

    for i in range(len(A)):
        if i % 2 == 0 :
            B.append(A[i])
    print(B)

    for j in range(len(B)):
        A.append(B[j])
    print("Доповнений список з парними елементами списку:")
    print(A)

add_paired()
