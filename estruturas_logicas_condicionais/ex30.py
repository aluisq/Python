a = round(float(input("Insira o primeiro número: ")),2)

b = round(float(input("Insira o segundo número: ")),2)

c = round(float(input("Insira o terceiro número: ")),2)

if a > b > c:
    print(f"{c}, {b}, {a}")
elif a > c > b:
    print(f"{b}, {c}, {a}")
elif b > a > c:
    print(f"{c}, {a}, {b}")
elif b > c > a:
    print(f"{a}, {c}, {b}")
elif c > a > b:
    print(f"{b}, {a}, {c}")
else:
    print(f"{a}, {b}, {c}")