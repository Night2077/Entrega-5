from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusServerContext, ModbusSlaveContext, ModbusSequentialDataBlock
from threading import Thread
from time import sleep
import asyncio

# Entrada Discreta
DI1 = 1
DI2 = 0

#
IR1 = 20
IR2 = 80

TEMPO = 1
TAXA_MUDANCA = 2
CONTINUA = True

PORT = 5020

escravos = ModbusSlaveContext(
    di = ModbusSequentialDataBlock(0,[DI1,IR1]),
    ir = ModbusSequentialDataBlock(0,[DI2,IR2])
)

context = ModbusServerContext(slaves=escravos,single=True)

async def run_processo():
    global IR1,IR2
    while CONTINUA:

        val = context[0].getValues(2,0,count=2)

        print(f"IR1:{val[0]},IR2:{val[1]}")
        
        if val[0] == 1:
            IR1 += TAXA_MUDANCA
        else:
            IR1 -= TAXA_MUDANCA
        
        if val[1] == 1:
            IR2 += TAXA_MUDANCA
        else:
            IR2 -= TAXA_MUDANCA

    IR1 = max(0,min(100,IR1))
    IR2 = max(0,min(100,IR2))

    context[0].setValues(4,0,[int(IR1),int(IR2)])

    await asyncio.sleep(TEMPO)

# main
async def main():
    await asyncio.gather(
        run_processo(),
        StartTcpServer(context,address=("localhost",5020))
    )


asyncio.run(main())
