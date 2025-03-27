print("Descubra se os valores informados formam um triângulo e qual o tipo dele.\n")
a = float(input("Informe um número: "))
b = float(input("Informe outro número: "))
c = float(input("Informe mais um número: "))
if a < b + c and b < a + c and c < a + b:
    if a == b and b == c:
        print("\nÉ um Triângulo Equilátero.")
    elif a == b or b == c or a == c:
        print("\nÉ um Triângulo Isósceles.")
    else:
        print("\nÉ um Triângulo Escaleno.")
else:
    print("\nNão é Triângulo.")