class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0,numero_cuenta=""):
        self.titular = titular
        self.saldo = saldo_inicial
        self.numero_cuenta=numero_cuenta

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")
            else:
                print("Fondos insuficientes para realizar el retiro.")
        else:
            print("La cantidad a retirar debe ser positiva.")

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo}")

    def crear_cuenta():
        titular = input("Ingrese el nombre del titular de la cuenta: ")
        numero_cuenta = input("Ingrese el número de cuenta: ")  
        cuenta = CuentaBancaria(titular, 0, numero_cuenta)

        print("Cuenta creada correctamente")

    def mostrar_cuenta(self):
        print(f"Titular: {self.titular}")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Saldo: {self.saldo}")



print("=======MENNU==========")
print("1: Crear Cuenta")
print("2: Mostrar Cuenta")
print("3: Depositar Dinero")
print("4: Retirar Dinero")
print("5: Salir")
opcion = int(input("Elige una opcion del 1 al 5: "))
while opcion >= 1 or opcion <= 5:
    #print("Opcion no valida, elige una opcion del 1 al 5")
    

    if opcion == 1:
        CuentaBancaria.crear_cuenta()
    elif opcion == 2:
        CuentaBancaria.mostrar_cuenta()
    elif opcion == 3:
        CuentaBancaria.depositar()

    elif opcion == 4:
        CuentaBancaria.retirar()
    elif opcion == 5:
        print("Saliendo del programa...")
    
    print("=======MENNU==========")
    print("1: Crear Cuenta")
    print("2: Mostrar Cuenta")
    print("3: Depositar Dinero")
    print("4: Retirar Dinero")
    print("5: Salir")
        
    opcion = int(input("Elige una opcion del 1 al 5: "))