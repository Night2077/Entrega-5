from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusServerContext, ModbusSlaveContext, ModbusSequentialDataBlock

#variaveis
COIL1 = 0
COIL2 = 1

PORT = 5020

# escravo
escravo = ModbusSlaveContext(
    CO = ModbusSequentialDataBlock(0,[COIL1,COIL2]),
    zero_mode = True
)

#contexto 
context = ModbusServerContext(slaves=escravo) 

print('servidor')
print(f'Porta:{PORT}')
print(f"co[0]= {COIL1}")
print(f"c[1]= {COIL2}")
print('_________')


# Start server
StartTcpServer(context,address=("localhost",PORT))



