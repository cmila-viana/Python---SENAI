cidade = int(input("Informe um número para escolher uma Capital do Nordeste: "))

def city (cidade):
    
    match(cidade):
        case 1:
            return "Salvador"
        case 2:
            return "Recife"
        case 3:
            return "Aracaju"
        case 4:
            return "Maceió"
        case 5:
            return "João Pessoa"
        case 6:
            return "Natal"
        case 7:
            return "São Luiz"
        case 8:
            return "Terezina"
        case 9:
            return "Ceará"
        case _:
            return "Opção inválida"
        
resultado = city(cidade)
print("O número escolhido corresponde a Capital", resultado)