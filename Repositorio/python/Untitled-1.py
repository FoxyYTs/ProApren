print ("hola mundo")
a = int(input())
b = int(input())
c = int(input())
if a == b and b == c:
    print (3)
elif a == b and b != c:
    print (2)
elif a != b and b == c:
    print (2)
elif a == c and c != b:
    print (2)
else:
    print(0)