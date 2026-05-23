from abc import abstractmethod, ABC
from typing import Any, Generic

from pymodbus.client import ModbusTcpClient
from pymodbus.pdu import ModbusPDU

from Protocol import T
from Reader import IReader
from Storage import IStorage
from main import device_id


def read_modbus_register(client: ModbusTcpClient, result: ModbusPDU, index: int, span: int,
                         data_type: Any = None):
    if data_type is None:
        data_type = client.DATATYPE.FLOAT32
    return client.convert_from_registers(
        registers=result.registers[index:index + span],
        data_type=data_type,
        word_order="big"
    )


class Pac3320ModbusDataFactory(ABC, Generic[T]):

    @abstractmethod
    def read_registers(self, client: ModbusTcpClient, device_id: int) -> T:
        pass


class Pac3220ModbusReader(IReader[T]):
    def __init__(self, ip: str, port: int, device_id: int, data_factory: Pac3320ModbusDataFactory[T],
                 storage_engine: IStorage[T]):
        self.ip = ip
        self.port = port
        self.device_id = device_id
        self.data_factory = data_factory
        super().__init__(storage_engine)

    def read(self) -> T:
        client = ModbusTcpClient(self.ip, port=self.port)
        if not client.connect():
            raise ConnectionError("Connection failed.")

        try:
            return self.data_factory.read_registers(client, device_id)
        except ConnectionError as e:
            raise e
        except Exception as e:
            raise RuntimeError(f"Unexpected error: {e}")
        finally:
            client.close()
