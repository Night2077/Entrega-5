from pymodbus.client.sync import ModbusTcpClient

DI_ADDRESS = 0
IR_ADDRESS = 0

SERVERS = [
    ("localhost", 5020),
    ("localhost", 5021)
]

print(f"Endereço DI: {DI_ADDRESS}")
print(f"Endereço IR: {IR_ADDRESS}")

# leitura de server
for ip, port in SERVERS:
    print(f"\nConectando ao servidor {ip}:{port}")

    cliente = ModbusTcpClient(ip, port)
    cliente.connect()

    di = cliente.read_discrete_inputs(DI_ADDRESS, 1).getBit(0) 
    ir = cliente.read_input_registers(IR_ADDRESS, 1).getRegister(0)

    print(f"DI = {di}")
    print(f"IR = {ir}")

    cliente.close()
