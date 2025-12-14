from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusServerContext, ModbusSlaveContext, ModbusSequentialDataBlock
from threading import Thread
from time import sleep


TEMPO = 2
TAXA_MUDANÇA = 5

IR1 = 10
IR2 = 50

PORT = 5020

CONTINUA = True

escravos = {
    0x00: ModbusSlaveContext(
        ir = ModbusSequentialDataBlock(0,[IR1]),
        zero_mode = True
    ),
    0x01: ModbusSlaveContext(
        ir = ModbusSequentialDataBlock(0,[IR2]),
        zero_mode = True
    )
}

context = ModbusServerContext(slaves=escravos,single=False)

def run_processo(context):
    global CONTINUA
    while CONTINUA:
        for unit_id in [0x00,0x01]:
            atual = context[unit_id].getValues(4,0)[0]
            novo = atual + TAXA_MUDANÇA
            context[unit_id].setValues(4,0,[novo])
            print(f"Escravo{unit_id}, IR[0]={novo}")
        sleep(TEMPO)

t = Thread(target=run_processo,args=(context,))
t.start()

try:
    print(f"Porta: {PORT}")
    StartTcpServer(context, address=("localhost", PORT))
finally:
    CONTINUA = False
    t.join()


# Start server
#StartTcpServer(context,address=("localhost",PORT))



