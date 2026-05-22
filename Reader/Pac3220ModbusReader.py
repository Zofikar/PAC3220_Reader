from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Any

from pymodbus.client import ModbusTcpClient
from pymodbus.pdu import ModbusPDU

from Protocol import Serializable
from Reader import IReader
from Storage import IStorage


@dataclass(frozen=True)
class Pac3320ModbusData(Serializable):
    L1_Voltage: float
    L1_Current: float
    TotalPower: float

    timestamp: str = ""

    def __post_init__(self):
        object.__setattr__(self, "timestamp", datetime.now().strftime("%d.%m.%Y %H:%M"))
        object.__setattr__(self, "L1_Voltage", round(self.L1_Voltage, 3))
        object.__setattr__(self, "L1_Current", round(self.L1_Current, 3))
        object.__setattr__(self, "TotalPower", round(self.TotalPower, 3))

    def to_dict(self):
        return asdict(self)


class Pac3220ModbusReader(IReader[Pac3320ModbusData]):
    def __init__(self, ip: str, port: int, device_id: int, storage_engine: IStorage[Pac3320ModbusData]):
        self.ip = ip
        self.port = port
        self.device_id = device_id
        super().__init__(storage_engine)

    @staticmethod
    def __read_modbus_register(client: ModbusTcpClient, result: ModbusPDU, index: int, span: int,
                               data_type: Any = None):
        if data_type is None:
            data_type = client.DATATYPE.FLOAT32
        return client.convert_from_registers(
            registers=result.registers[index:index + span],
            data_type=data_type,
            word_order="big"
        )

    def read(self) -> Pac3320ModbusData:
        client = ModbusTcpClient(self.ip, port=self.port)
        if not client.connect():
            raise ConnectionError("Connection failed.")

        try:
            result = client.read_holding_registers(address=0, count=66, device_id=self.device_id)
            if result.isError():
                raise ConnectionError(f"Modbus read failed: {result}")
            data = Pac3320ModbusData(
                L1_Voltage=self.__read_modbus_register(client, result, 0, 2),
                L1_Current=self.__read_modbus_register(client, result, 12, 2),
                TotalPower=self.__read_modbus_register(client, result, 64, 2)
            )
            return data
        except ConnectionError as e:
            raise e
        except Exception as e:
            raise RuntimeError(f"Unexpected error: {e}")
        finally:
            client.close()
