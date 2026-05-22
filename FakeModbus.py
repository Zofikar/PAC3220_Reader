import asyncio
import logging

# Clean imports from modern root package namespace
from pymodbus import ModbusDeviceIdentification
from pymodbus.server import StartAsyncTcpServer
from pymodbus.simulator import SimData, SimDevice, DataType

# Configure logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)


async def run_mock_server(ip="127.0.0.1", port=5020):
    """
    Runs a Mock Modbus TCP Server populated with PAC3220 simulator data.
    """

    # 1. Directly feed Python floats to SimData using DataType.FLOAT32!
    # Pymodbus will automatically handle splitting these across 2 sequential registers.
    # Note: Address 0 = Register 1, Address 12 = Register 13, Address 64 = Register 65.
    sim_data_list = [
        SimData(address=0, values=230.5, datatype=DataType.FLOAT32),  # L1_Voltage (Uses addresses 0 & 1)
        SimData(address=12, values=5.25, datatype=DataType.FLOAT32),  # L1_Current (Uses addresses 12 & 13)
        SimData(address=64, values=1500.0, datatype=DataType.FLOAT32)  # Total Active Power (Uses addresses 64 & 65)
    ]

    # 2. Fill the remaining slots with dummy placeholder numbers.
    # Since DataType.REGISTERS expects signed numbers, we can use small, clean increments.
    used_addresses = {0, 1, 12, 13, 64, 65}
    for addr in range(100):
        if addr not in used_addresses:
            sim_data_list.append(SimData(address=addr, values=[addr + 1], datatype=DataType.REGISTERS))

    # 3. Explicitly instantiate SimDevice with Device ID 1
    device_store = SimDevice(1, sim_data_list)

    # Dictionary style for device identity
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

    print(f"Starting Mock PAC3220 Server on {ip}:{port}")
    print("The server is running. Press Ctrl+C to stop.")

    # 4. Spin up the server passing the modern device configuration list directly
    await StartAsyncTcpServer(
        context=[device_store],
        identity=identity,
        address=(ip, port)
    )


if __name__ == "__main__":
    try:
        asyncio.run(run_mock_server())
    except KeyboardInterrupt:
        print("\nServer stopped by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")