class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0, numero_cuenta=""):
        self.titular = titular
        self.saldo = saldo_inicial
        self.numero_cuenta = numero_cuenta

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

    def mostrar_cuenta(self):
        print(f"Titular: {self.titular}")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Saldo: {self.saldo}")


cuenta = None

while True:
    print("======= MENÚ ==========")
    print("1: Crear Cuenta")
    print("2: Mostrar Cuenta")
    print("3: Depositar Dinero")
    print("4: Retirar Dinero")
    print("5: Salir")

    opcion = int(input("Elige una opción del 1 al 5: "))

    if opcion == 1:
        titular = input("Ingrese el nombre del titular: ")
        numero = input("Ingrese el número de cuenta: ")
        cuenta = CuentaBancaria(titular, 0, numero)
        print("Cuenta creada correctamente.")

    elif opcion == 2:
        if cuenta:
            cuenta.mostrar_cuenta()
        else:
            print("Primero debes crear una cuenta.")

    elif opcion == 3:
        if cuenta:
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cuenta.depositar(cantidad)
        else:
            print("Primero debes crear una cuenta.")

    elif opcion == 4:
        if cuenta:
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cuenta.retirar(cantidad)
        else:
            print("Primero debes crear una cuenta.")

    elif opcion == 5:
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")