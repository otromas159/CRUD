s = int(input("ingrese 1 o 2: "))

if s == "1":
    print("El color es azul")
elif s == "2":
    print("El color es rojo")
else:
    print("El color es verde")


print("ciclo for")
for s in range(1, 6):
    print(s)

print("ciclo while")
while s < 5:
    print(s)
    s += 1
