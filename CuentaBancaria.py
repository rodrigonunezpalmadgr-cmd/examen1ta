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
        print("Cuenta creada correctamente")

    def mostrar_cuenta():
        print("Mostrar cuenta")        

print("=======MENNU==========")
print("Crear Cuenta")
print("Mostrar Cuenta")
print("Depositar Dinero")
print("Retirar Dinero")
print("Salir")

opcion = int(input("Elige una opcion del 1 al 5: "))
if opcion == 1:
    CuentaBancaria.crear_cuenta()
elif opcion == 2:
    CuentaBancaria.mostrar_cuenta()
elif opcion == 3:
    CuentaBancaria.depositar()

elif opcion == 4:
    CuentaBancaria.retirar()
else:
    print("Esta opcion no es valida")                      