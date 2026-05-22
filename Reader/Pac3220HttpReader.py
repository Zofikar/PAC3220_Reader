from dataclasses import dataclass, asdict
from datetime import datetime

import requests

from Protocol import Serializable
from Reader import IReader
from Storage import IStorage


@dataclass(frozen=True)
class Pac3320HttpData(Serializable):
    L1_Voltage: float
    L1_Current: float
    TotalPower: float

    timestamp: str = ""

    def __post_init__(self):
        if self.timestamp == "":
            object.__setattr__(self, "timestamp", datetime.now().strftime("%d.%m.%Y %H:%M"))
        object.__setattr__(self, "L1_Voltage", round(self.L1_Voltage, 3))
        object.__setattr__(self, "L1_Current", round(self.L1_Current, 3))
        object.__setattr__(self, "TotalPower", round(self.TotalPower, 3))

    def to_dict(self):
        return asdict(self)


class Pac3220HttpReader(IReader[Pac3320HttpData]):
    def __init__(self, ip: str, port: int, storage_engine: IStorage[Pac3320HttpData]):
        self.ip = ip
        self.port = port
        super().__init__(storage_engine)

    def read(self) -> Pac3320HttpData:
        # noinspection HttpUrlsUsage
        url = f"http://{self.ip}:{self.port}/data.json"
        params = {"type": "INST"}
        try:
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()

            inst_values = response.json().get("INST_VALUES", {})

            return Pac3320HttpData(
                L1_Voltage=float(inst_values["V_L1"]["value"]),
                L1_Current=float(inst_values["I_L1"]["value"]),
                TotalPower=float(inst_values["P_TOT"]["value"]),
                timestamp=inst_values.get("LOCAL_TIME", "")
            )

        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Error reading PAC3220: {e}")
        except KeyError as e:
            raise ValueError(f"PAC3220 JSON structure missing expected key: {e}")
