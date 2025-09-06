print("MEDIDOR DE CONSUMO")

marca = input("forneça a marca do veiculo: ")
modelo = input("forneça o modelo do veiculo:")
km = float(input("km's percorridos: "))
lts = float(input("quantidade de litros gastos: "))

consumo = km / lts

if consumo < 6:
    FdC = ("Altissimo consumo")
    print(f"{marca} {modelo} fez {consumo} km/L e isso é considerado um {FdC}")
elif consumo > 6 and consumo <= 9:
    FdC = ("Alto consumo")
    print(f"{marca} {modelo} fez {consumo} km/L e isso é considerado um {FdC}")
elif consumo > 9 and  consumo <= 12:
    FdC = ("Médio consumo")
    print(f"{marca} {modelo} fez {consumo} km/L e isso é considerado um {FdC}")
elif consumo > 12 and consumo <= 15:
    FdC = ("Bom consumo")
    print(f"{marca} {modelo} fez {consumo} km/L e isso é considerado um {FdC}")
elif consumo > 15:
    FdC = ("Ótimo consumo")
    print(f"{marca} {modelo} fez {consumo} km/L e isso é considerado um {FdC}")
    


    

