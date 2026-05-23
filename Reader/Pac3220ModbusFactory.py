import logging
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from pymodbus.client import ModbusTcpClient

from Protocol.Protocol import DictWrapper
from .Pac3220ModbusReader import Pac3320ModbusDataFactory

logger = logging.getLogger(__name__)

@dataclass(frozen=True)
class ModbusTcpRegister:
    name: str
    address: int
    data_type: ModbusTcpClient.DATATYPE = ModbusTcpClient.DATATYPE.FLOAT32

    @staticmethod
    def from_dict(dct):
        dct["data_type"] = ModbusTcpClient.DATATYPE.__members__[dct["data_type"]]
        return ModbusTcpRegister(**dct)

    @property
    def size(self):
        return self.data_type.value[1]


def read_modbus_register(client: ModbusTcpClient, register: ModbusTcpRegister, device_id: int):
    value = client.read_holding_registers(register.address, count=register.size, device_id=device_id)
    return client.convert_from_registers(
        registers=value.registers,
        data_type=register.data_type,
        word_order="big"
    )

class Pac3220ModbusFactory(Pac3320ModbusDataFactory[DictWrapper]):
    def __init__(self, registers: list[ModbusTcpRegister]):
        super().__init__()
        self.registers = registers

    def read_registers(self, client: ModbusTcpClient, device_id: int) -> DictWrapper:
        data: dict[str, Any] = {
            "timestamp": datetime.now().strftime("%d.%m.%Y %H:%M")
        }
        for register in self.registers:
            try:
                data[register.name] = read_modbus_register(client, register, device_id)
            except Exception as e:
                logger.error(e)
                data[register.name] = -1
        return DictWrapper(data)
