from dataclasses import dataclass
from datetime import datetime

from pymodbus.client import ModbusTcpClient
from pymodbus.pdu import ModbusPDU

from Protocol.Protocol import DictWrapper
from .Pac3220ModbusReader import Pac3320ModbusDataFactory, read_modbus_register


@dataclass(frozen=True)
class ModbusTcpRegister:
    name: str
    address: int
    data_type: ModbusTcpClient.DATATYPE = ModbusTcpClient.DATATYPE.FLOAT32

    @staticmethod
    def from_dict(dct):
        dct["data_type"] = ModbusTcpClient.DATATYPE.__members__[dct["data_type"]]
        return ModbusTcpRegister(**dct)


class Pac3220ModbusFactory(Pac3320ModbusDataFactory[DictWrapper]):
    def __init__(self, registers: list[ModbusTcpRegister]):
        super().__init__()
        self.registers = registers

    def read_registers(self, client: ModbusTcpClient, result: ModbusPDU) -> DictWrapper:
        data = {
            "timestamp": datetime.now().strftime("%d.%m.%Y %H:%M")
        }
        for register in self.registers:
            data[register.name] = read_modbus_register(client, result, register.address, register.data_type.value[1],
                                                       register.data_type)
        return DictWrapper(data)
