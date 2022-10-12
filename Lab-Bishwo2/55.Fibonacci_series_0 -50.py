a = 0
b = 1
fibo = 0

print(a, end=" ")
print(b, end=" ")

for i in range(2, 50):
    fibo = a + b
    a = b
    b = fibo
    print(fibo, end=" ")