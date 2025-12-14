from pymodbus.client.sync import ModbusTcpClient
from pymodbus.pdu import ModbusExceptions

SERVERS = [
    ("localhost", 5020),
]

# Invalida 02
INVALID_ADRESS = 10
INVALID_CONT1 = 1

# Invalida 03
VALID_ADRESS = 0
INVALID_CONT2 = 300

# Valida 
VALID_CONT = 2
VALID_VALUES = [1,0]

for ip, port in SERVERS:
    print(f"\nConectando ao servidor {ip}:{port}")
    cliente = ModbusTcpClient(ip, port)
    cliente.connect()

    # Execeção 02 
    print("\nTeste exceção 0x02 (endereço inválido)")
    print(f"Endereço={INVALID_ADRESS}, Quantidade={INVALID_CONT1}")
    requisicao = cliente.write_coils(INVALID_ADRESS, [0]*INVALID_CONT1)
    if requisicao.isError():
        print("Exceção:", ModbusExceptions.decode(requisicao.exception_code))

    # Execeção 03
    print("\nTeste exceção 0x03 (quantidade inválida)")
    print(f"Endereço={VALID_ADRESS}, Quantidade={INVALID_CONT2}")
    requisicao = cliente.write_coils(VALID_ADRESS, [0]*INVALID_CONT2)
    if requisicao.isError():
        print("Exceção:", ModbusExceptions.decode(requisicao.exception_code))

    # Escrita Valida
    print("\nEscrita válida")
    print(f"Endereço={VALID_ADRESS}, Valores={VALID_VALUES}")
    cliente.write_coils(VALID_ADRESS, VALID_VALUES)

    # Leitura 
    print("\nLeitura")
    resp = cliente.read_coils(VALID_ADRESS, VALID_CONT)
    print("Valores lidos:", resp.bits[:VALID_CONT])

    cliente.close()
