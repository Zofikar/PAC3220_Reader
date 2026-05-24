#!/usr/bin/env python3
import asyncio
import logging
import random

from pymodbus import ModbusDeviceIdentification
from pymodbus.client import ModbusTcpClient
from pymodbus.server import StartAsyncTcpServer
from pymodbus.simulator import SimData, SimDevice, DataType

from Reader.modbus_map import REGISTER_MAP

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)


def to_enum(dt: ModbusTcpClient.DATATYPE) -> DataType:
    return DataType[dt.name]


def get_address_signature_value(address: int, modbus_type: DataType) -> float | int:
    """
    Generates a uniquely recognizable numeric pattern based directly on the register address.
    """
    drift = random.uniform(0, 0.05)

    if modbus_type == DataType.FLOAT32:
        # e.g., Address 13 (Current L1) -> 13.13 + drift
        base = address + (address / 100.0) if address < 100 else address + (address / 1000.0)
        return round(base + drift, 4)

    elif modbus_type == DataType.FLOAT64:
        # e.g., Address 801 (Energy Import) -> 801.801 + drift
        base = address + (address / 1000.0)
        return round(base + drift, 6)

    elif modbus_type in (DataType.UINT32, DataType.INT32):
        # e.g., Address 203 (Limit violations) -> 203
        # No floating point drift for integers, but maybe an integer step change
        return address

    else:
        return address


async def run_mock_server(ip="127.0.0.1", port=5020):
    """
    Runs a Mock Modbus TCP Server fully populated by your auto-generated REGISTER_MAP.
    """
    sim_data_list = []

    # Process the entire generated map dynamically
    for address, (name, client_type) in REGISTER_MAP.items():
        py_modbus_type = to_enum(client_type)
        mock_value = get_address_signature_value(address, py_modbus_type)

        sim_data_list.append(
            SimData(
                address=address,
                values=mock_value,
                datatype=py_modbus_type
            )
        )
        log.debug(f"Mapped {name} at address {address} -> Value: {mock_value}")

    # Build the memory space using the parsed SimData chunks
    device_store = SimDevice(1, sim_data_list)

    identity = ModbusDeviceIdentification(
        info_name={
            "VendorName": "Siemens",
            "ProductCode": "PAC3220",
            "VendorUrl": "https://siemens.com",
            "ProductName": "Power Meter Simulator",
            "ModelName": "PAC3220",
            "MajorMinorRevision": "3.13",
        }
    )

    print(f"\n[SUCCESS] Loaded {len(REGISTER_MAP)} registers from REGISTER_MAP.")
    print(f"Starting Mock PAC3220 Server on {ip}:{port}")
    print("Press Ctrl+C to stop.")

    await StartAsyncTcpServer(
        context=[device_store],
        identity=identity,
        address=(ip, port)
    )


if __name__ == "__main__":
    try:
        # Run on local testing loop port 5020
        asyncio.run(run_mock_server("127.0.0.1", 5020))
    except KeyboardInterrupt:
        print("\nServer stopped safely.")
