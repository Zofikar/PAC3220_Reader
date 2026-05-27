import logging
from datetime import datetime
from typing import Any

from pymodbus.client import ModbusTcpClient

from ModbusDefinition import REGISTER_MAP
from Protocol.Protocol import DictWrapper
from .Pac3220ModbusReader import Pac3320ModbusDataFactory

logger = logging.getLogger(__name__)


def get_size(dtype: ModbusTcpClient.DATATYPE) -> int:
    return dtype.value[1]


def read_modbus_register(client: ModbusTcpClient, register: int, dtype: ModbusTcpClient.DATATYPE, device_id: int):
    value = client.read_holding_registers(register, count=get_size(dtype), device_id=device_id)
    return client.convert_from_registers(
        registers=value.registers,
        data_type=dtype,
        word_order="big"
    )

class Pac3220ModbusFactory(Pac3320ModbusDataFactory[DictWrapper]):
    def __init__(self, registers: list[int]):
        super().__init__()
        self.registers = registers

    def read_registers(self, client: ModbusTcpClient, device_id: int) -> DictWrapper:
        data: dict[str, Any] = {
            "timestamp": datetime.now().strftime("%d.%m.%Y %H:%M")
        }
        for register in self.registers:
            name, dtype = REGISTER_MAP[register]
            try:
                data[name] = read_modbus_register(client, register, dtype, device_id)
            except Exception as e:
                logger.error(e)
                data[name] = -1
        return DictWrapper(data)
