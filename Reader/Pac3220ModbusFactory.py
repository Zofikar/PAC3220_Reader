from dataclasses import dataclass
from datetime import datetime

from pymodbus.client import ModbusTcpClient
from pymodbus.pdu import ModbusPDU

from Pac3220ModbusReader import Pac3320ModbusDataFactory, read_modbus_register
from Protocol.Protocol import DictWrapper


@dataclass(frozen=True)
class ModbusTcpRegister:
    name: str
    address: int
    span: int = 2
    data_type: ModbusTcpClient.DATATYPE = ModbusTcpClient.DATATYPE.FLOAT32

    @staticmethod
    def from_dict(dct):
        dct["data_type"] = ModbusTcpClient.DATATYPE(dct["data_type"])
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
            data[register.name] = read_modbus_register(client, result, register.address, register.span,
                                                       register.data_type)
        return DictWrapper(data)
