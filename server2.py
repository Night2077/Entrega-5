from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusServerContext, ModbusSlaveContext, ModbusSequentialDataBlock

DI_VALUE = 0
IR_VALUE = 75

PORT = 5021

# 
escravo = ModbusSlaveContext(
    di = ModbusSequentialDataBlock(0,[DI_VALUE]), 
    ir = ModbusSequentialDataBlock(0,[IR_VALUE]),
    zero_mode = True
)

context = ModbusServerContext(slaves=escravo) #


print('servidor')
print(f'Porta:{PORT}')
print('_________')


# Start server
StartTcpServer(context,address=("localhost",PORT))