n = int(input("Введіть розмір масиву:"))
s = []
for i in range(n):
    i = int(input("Новий елемент масиву: "))
    s.append(i)

print(s)

negative = [j for j in s if j < 0]

print("Максимальниц елемент масиву:", max(negative))

