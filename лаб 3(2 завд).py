s = input("Введіть слово: ")
n = ''
i = 0
while i < len(s):
    if i == 0:
        if s[i] != s[i + 1]:
            n += s[i]
    if i == len(s) - 1:
        if s[i] != s[i - 1]:
            n += s[i]
    else:
        if s[i] != s[i - 1] and s[i] != s[i + 1]:
            n += s[i] 
    i += 1

print("Слово з видаленими однаковими символами, які розташовані поруч: ", n)