# creamos un arreglo de transacciones con fecha, cliente, tipo, monto y moneda
transacciones = [
    ("2024-01-10", "Ana", "deposito", 5000, "MXN"),
    ("2024-01-12", "Luis", "retiro", 1500, "MXN"),
    ("2024-01-15", "Ana", "retiro", 2000, "MXN"),
    ("2024-01-18", "Carlos", "deposito", 7000, "MXN")
]
# creamos un diccionario para almacenar los balances de cada cliente
balances = {}

# unpacking directo en el for
for fecha, cliente, tipo, monto, moneda in transacciones:
    # verificamos si el cliente ya tiene un balance, si no lo inicializamos
    if cliente not in balances:
        balances[cliente] = 0
    # actualizamos el balance según el tipo de transacción usando unpacking
    if tipo == "deposito":
        balances[cliente] += monto
        #en caso ede retiro, restamos el monto al balance del cliente
    else:
        balances[cliente] -= monto

# imprimimos los balances finales usando unpacking
print(f"\nBalances finales:\n")

# impresión con unpacking
# iteramos sobre el diccionario de balances usando unpacking para obtener el cliente y su balance
for cliente, balance in balances.items():
    print(f"Cliente: {cliente} = Balance: {balance}")


# unpacking al obtener el mayor
# obtenemos el cliente con el mayor balance usando unpacking
#esta parte no le entendí mucho, pero básicamente se usa max con una función lambda para comparar los balances y obtener el cliente con el mayor balance
mejor_cliente, mejor_balance = max(balances.items(), key=lambda x: x[1])

# imprimimos el cliente con el mayor balance usando unpacking
print(f"\nMayor balance: {mejor_cliente} con {mejor_balance}")
