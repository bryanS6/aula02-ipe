print("Verificador de idade")
nome = input("Qual seu nome?")
idade = int(input("Qual sua idade?"))

if idade > 18:
    print(nome + " você é maior de idade")
elif idade == 18:
    print(nome + "é maior de idade com exatamente 18 anos")
else:
    print(nome + " você é menor de idade")

peso = float(input("Insira seu peso em kg: "))
altura = float(input("Insira sua altura em metros: "))


try: 
    imc = peso / (altura * altura) 
    if imc <= 18.5:
        print(f"{nome} seu IMC é de: {imc} portanto, você está abaixo do peso")
    elif imc <= 24.9:
        print(f"{nome} seu IMC é de: {imc} portanto, você está dentro do peso ideal")
    elif imc <= 29.9:
        print(f"{nome} seu IMC é de: {imc} portanto, você está com sobrepeso")
    else:
         print(f"{nome} seu IMC é de: {imc} portanto, você está com obesidade")
except ZeroDivisionError:
    print("O programa não é capaz de dividir por zero!")

    