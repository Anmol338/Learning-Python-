a = 12
print(type(a))
b = int(input())
if type(a) == type(b):
    print(b)
elif type(a) != type(b):
    print("Invalid type")