#Cuenta: 111 o 222  Clave:123 debe colocarlos para poder usar el cajero.

class Banco:
    def __init__(self, nombre):
        self.nombre = nombre

class Cuenta:
    def __init__(self, numero_cuenta, saldo, limite_credito, tipo_cuenta):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.limite_credito = limite_credito
        self.tipo_cuenta = tipo_cuenta

class Cliente:
    def __init__(self, nombre, direccion, numero_cuenta, saldo_inicial):  
        self.nombre = nombre
        self.direccion = direccion
        self.cuenta = Cuenta(numero_cuenta, saldo_inicial, 0, "Corriente")

class Cajero:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

class CajeroAutomatico:
    def __init__(self, banco, clientes):
        self.banco = banco
        self.clientes = {cliente.cuenta.numero_cuenta: cliente for cliente in clientes}

    def _validar_usuario(self, numero_cuenta, contraseña):
        cliente = self.clientes.get(numero_cuenta)
        return cliente is not None and contraseña == "123"

    def _realizar_operacion(self, numero_cuenta, contraseña, operacion, *args):
        if self._validar_usuario(numero_cuenta, contraseña):
            cliente = self.clientes[numero_cuenta]
            operacion(cliente, *args)
        else:
            print("Usuario o contraseña incorrectos.")

    def retirar_efectivo(self, cliente, cantidad):
        if cantidad <= cliente.cuenta.saldo:
            cliente.cuenta.saldo -= cantidad
            print(f"Retirada exitosa. Nuevo saldo: {cliente.cuenta.saldo}")
        else:
            print("Saldo insuficiente para esta operación.")

    def ingresar_efectivo(self, cliente, cantidad):
        cliente.cuenta.saldo += cantidad
        print(f"Ingreso de efectivo exitoso. Nuevo saldo: {cliente.cuenta.saldo}")

    def pagar_factura(self, cliente, info_factura):
        print(f"Factura pagada por {cliente.nombre}: {info_factura}")

    def transferir_fondos(self, cliente, cuenta_destino, cantidad):
        if cantidad <= cliente.cuenta.saldo:
            cliente.cuenta.saldo -= cantidad
            print(f"Transferencia exitosa. Nuevo saldo: {cliente.cuenta.saldo}")
        else:
            print("Saldo insuficiente para esta transferencia.")

# Usuarios
cliente1 = Cliente("Juan", "Enrriquillo", "222", 50000)
cliente2 = Cliente("Pedro", "Sabana Grande #25", "111", 30000)

# Uso del cajero automático
banco_principal = Banco("Banco Tech")
clientes = [cliente1, cliente2]

cajero_principal = Cajero("Cajero Principal", "1234")
cajero_automatico = CajeroAutomatico(banco_principal, clientes)

# Bienvenida al banco
print(f"Bienvenido a {banco_principal.nombre}.")

while True:
    # Solicitud
    print("\nIngrese 'Salir' en cualquier momento para salir del cajero.\n")
    numero_cuenta = input("\nIngrese el número de cuenta: ")

    if numero_cuenta.lower() == 'salir':
        print("¡Hasta luego!")
        break

    contraseña = input("Ingrese la contraseña: ")

    # Validar 
    if cajero_automatico._validar_usuario(numero_cuenta, contraseña):
        print(f"\nUsuario identificado como {cajero_automatico.clientes[numero_cuenta].nombre}.\n")
        
        # Solicitar 
        print("¿Qué desea hacer?")
        print("1. Retirar efectivo")
        print("2. Ingresar efectivo")
        print("3. Pagar factura")
        print("4. Transferir fondos")
        print("5. Salir\n")
        
        opcion = input("Ingrese el número de la operación que desea realizar: ")

        if opcion == '5':
            print("¡Hasta luego!")
            break

        opcion = int(opcion)
        cliente = cajero_automatico.clientes[numero_cuenta]

        if opcion == 1:
            cantidad = float(input("Ingrese la cantidad que desea retirar: "))
            cajero_automatico.retirar_efectivo(cliente, cantidad)
        elif opcion == 2:
            cantidad = float(input("Ingrese la cantidad que desea ingresar: "))
            cajero_automatico.ingresar_efectivo(cliente, cantidad)
        elif opcion == 3:
            info_factura = input("Ingrese la información de la factura: ")
            cajero_automatico.pagar_factura(cliente, info_factura)
        elif opcion == 4:
            cuenta_destino = input("Ingrese el número de cuenta destino: ")
            cantidad = float(input("Ingrese la cantidad que desea transferir: "))
            cajero_automatico.transferir_fondos(cliente, cuenta_destino, cantidad)
        else:
            print("Opción no válida.")
    else:
        print("Usuario o contraseña incorrectos.")


