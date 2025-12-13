from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusServerContext, ModbusSlaveContext, ModbusSequentialDataBlock




loja = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*2), zero_mode=True)
contexto = ModbusServerContext(slaves=loja)





