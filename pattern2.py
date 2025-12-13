n = int(input("Enter a number: "))
var = ""
x = ""
for i in range(1, n + 2):
    var = str(i)
    x = x + var

for i in range(1, n + 1):
    x = x [:-1]
    print(x)