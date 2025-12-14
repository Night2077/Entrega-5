from pymodbus.client.sync import ModbusTcpClient
from pymodbus.pdu import ModbusExceptions
from time import sleep


SERVERS = [
    ("localhost", 5020),
]

IR_ADDRESS = 0
CONT = 1


for ip, port in SERVERS:
    print(f"\nConectando ao servidor {ip}:{port}")
    cliente = ModbusTcpClient(ip, port)
    cliente.connect()

    for unit in [0x00,0x01]:
        resp = cliente.read_input_registers(IR_ADDRESS,CONT,unit=unit)
        print(f"Escravo {unit},IR[0] = {resp.registers[0]}")
    
    sleep(2)

    for unit in [0x00,0x01]:
        resp = cliente.read_input_registers(IR_ADDRESS,CONT,unit=unit)
        print(f"Escravo {unit},IR[0] = {resp.registers[0]}")

    cliente.close()

#teste de commit

    '''
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
    '''