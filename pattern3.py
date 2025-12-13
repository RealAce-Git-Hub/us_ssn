n = int(input("Enter a number: "))
var = ""
x = ""

for i in range(n):
    for j in range(1, n + 1):
        var = str(j)
        x = x + var

    for k in range(1, n):
        var = str(n - k)
        x = x + var

    print(" " * i + x)
    x = ""
    n = n - 1