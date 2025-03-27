n1 = float (input("Informe um número: "))
op = input("Informe uma das operações (+, -, /, *): ")
n2 = float (input("Informe outro número: "))

def operacao(n1,op,n2):
    
    match(op):
        case "+": 
            return n1 + n2
        case "-":
            return n1 - n2
        case "*":
            return n1 * n2
        case "/":
            return n1 / n2
        case _:
            return "Opção Inválida"
        
resultado = operacao(n1,op,n2)
print(f"O resultado do cálculo é: ", resultado)