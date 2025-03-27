from src.data.register_data import RegisterData

register = RegisterData("feeling_data.csv")


option = int(input("Adicionar dados negativos (1) ou positivos (2)?"))
while True:
    feeling = input("Insira: ")
    if option == 1:
        register.registerNegative(feeling)
    elif option == 2:
        register.registerPositive(feeling)
    else:
        break
    print("Registrado!")